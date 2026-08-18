function filterCerts(category) {
    const tabs = document.querySelectorAll('.cert-tab');
    const cards = document.querySelectorAll('.cert-card');

    // Update active tab styling
    tabs.forEach(tab => {
        if (tab.id === 'tab-' + category) {
            tab.classList.add('bg-theme-cyan/20', 'border-theme-cyan/50', 'text-white');
            tab.classList.remove('text-gray-400', 'hover:bg-white/5', 'border-transparent');
        } else {
            tab.classList.remove('bg-theme-cyan/20', 'border-theme-cyan/50', 'text-white');
            tab.classList.add('text-gray-400', 'hover:bg-white/5', 'border-transparent');
        }
    });

    // Filter cards
    cards.forEach(card => {
        if (category === 'all' || card.classList.contains(category)) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });
}

function openModal(imageSrc) {
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImage');
    
    modalImg.src = imageSrc;
    modal.classList.remove('hidden');
    
    // Trigger reflow for animation
    void modal.offsetWidth;
    
    modal.classList.remove('opacity-0');
    modalImg.classList.remove('scale-95');
    modalImg.classList.add('scale-100');
}

function closeModal() {
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImage');
    
    modal.classList.add('opacity-0');
    modalImg.classList.remove('scale-100');
    modalImg.classList.add('scale-95');
    
    setTimeout(() => {
        modal.classList.add('hidden');
    }, 300); // Wait for transition to finish
}

// Close modal on click outside image
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('imageModal');
    if (modal) {
        modal.addEventListener('click', function(e) {
            if (e.target === this) {
                closeModal();
            }
        });
    }
});

// Project Carousel Logic
let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.carousel-slide');
    const dots = document.querySelectorAll('.carousel-dot');
    
    if (slides.length === 0) return;
    
    // Handle wrap-around
    if (index >= slides.length) currentSlide = 0;
    else if (index < 0) currentSlide = slides.length - 1;
    else currentSlide = index;
    
    // Update slides
    slides.forEach((slide, i) => {
        if (i === currentSlide) {
            slide.classList.remove('hidden');
            slide.classList.add('block');
        } else {
            slide.classList.remove('block');
            slide.classList.add('hidden');
        }
    });
    
    // Update dots
    dots.forEach((dot, i) => {
        if (i === currentSlide) {
            dot.classList.remove('bg-white/40');
            dot.classList.add('bg-theme-cyan', 'shadow-[0_0_8px_rgba(0,229,255,0.8)]');
        } else {
            dot.classList.remove('bg-theme-cyan', 'shadow-[0_0_8px_rgba(0,229,255,0.8)]');
            dot.classList.add('bg-white/40');
        }
    });
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

function prevSlide() {
    showSlide(currentSlide - 1);
}

function goToSlide(index) {
    showSlide(index);
}



// ----------------------------------------------------
// Unified Interactive Background (Nebula + Particle Wave)
// ----------------------------------------------------
function initBackground() {
    // 1. Setup Canvas and Three.js Environment
    const container = document.getElementById("particle-canvas"); // we'll use the existing canvas div
    if (!container || typeof THREE === 'undefined') return;

    const winWidth = window.innerWidth;
    const winHeight = window.innerHeight;
    const aspectRatio = winWidth / winHeight;

    // Use PerspectiveCamera so the ParticleWave looks 3D, 
    // but the Nebula Plane will fill the screen behind it.
    const camera = new THREE.PerspectiveCamera(75, aspectRatio, 0.01, 1000);
    camera.position.set(0, 6, 5);

    const scene = new THREE.Scene();

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(winWidth, winHeight);
    container.appendChild(renderer.domElement);

    const clock = new THREE.Clock();

    // ==========================================
    // 2. NEBULA SHADER (Background)
    // ==========================================
    const nebulaVertex = `
      varying vec2 vUv;
      void main() {
        vUv = uv;
        // Since we are using a PerspectiveCamera, we want the nebula plane 
        // to act as a pure background screen. We can bypass modelViewMatrix 
        // and just draw it directly to clip space.
        gl_Position = vec4(position.xy, 0.99, 1.0); // Z=0.99 puts it at the far back
      }
    `;

    const nebulaFragment = `
      precision mediump float;
      uniform vec2 iResolution;
      uniform float iTime;
      uniform vec2 iMouse;
      uniform bool hasActiveReminders;
      uniform bool hasUpcomingReminders;
      uniform bool disableCenterDimming;
      varying vec2 vUv;

      #define t iTime
      mat2 mRot(float a){ float c=cos(a), s=sin(a); return mat2(c,-s,s,c); }
      float map(vec3 p){
        vec2 mo = iMouse / iResolution;
        if (length(iMouse) < 1.0) mo = vec2(0.5); // Default center

        // Rotate scene based on time AND mouse position (reduced effect)
        p.xz *= mRot(t*0.4 + (mo.x - 0.5)*0.8);
        p.xy *= mRot(t*0.3 + (mo.y - 0.5)*0.8);
        
        vec3 q = p*2. + t;
        return length(p + vec3(sin(t*0.7))) * log(length(p)+1.0)
             + sin(q.x + sin(q.z + sin(q.y))) * 0.5 - 1.0;
      }

      void mainImage(out vec4 O, in vec2 fragCoord) {
        vec2 uv = fragCoord / min(iResolution.x, iResolution.y) - vec2(.9, .5);
        uv.x += .4;
        vec3 col = vec3(0.0);
        float d = 2.5;

        for (int i = 0; i <= 5; i++) {
          vec3 p = vec3(0,0,5.) + normalize(vec3(uv, -1.)) * d;
          float rz = map(p);
          float f  = clamp((rz - map(p + 0.1)) * 0.5, -0.1, 1.0);

          vec3 base = hasActiveReminders
            ? vec3(0.05,0.2,0.5) + vec3(4.0,2.0,5.0)*f
            : hasUpcomingReminders
            ? vec3(0.05,0.3,0.1) + vec3(2.0,5.0,1.0)*f
            : vec3(0.1,0.3,0.4) + vec3(5.0,2.5,3.0)*f;

          col = col * base + smoothstep(2.5, 0.0, rz) * 0.7 * base;
          d += min(rz, 1.0);
        }

        float dist   = distance(fragCoord, iResolution*0.5);
        float radius = min(iResolution.x, iResolution.y) * 0.5;
        float dim    = disableCenterDimming
                     ? 1.0
                     : smoothstep(radius*0.3, radius*0.5, dist);

        O = vec4(col, 1.0);
        
        if (!disableCenterDimming) {
          O.rgb = mix(O.rgb * 0.3, O.rgb, dim);
        }
      }

      void main() {
        mainImage(gl_FragColor, vUv * iResolution);
      }
    `;

    const nebulaUniforms = {
      iTime: { value: 0 },
      iResolution: { value: new THREE.Vector2() },
      iMouse: { value: new THREE.Vector2() },
      hasActiveReminders: { value: false },
      hasUpcomingReminders: { value: false },
      disableCenterDimming: { value: false },
    };

    const nebulaMaterial = new THREE.ShaderMaterial({
      vertexShader: nebulaVertex,
      fragmentShader: nebulaFragment,
      uniforms: nebulaUniforms,
      depthWrite: false // Prevents background from covering particles
    });
    
    const nebulaMesh = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), nebulaMaterial);
    // Note: We bypass matrix transforms in the vertex shader, so it's always fullscreen.
    scene.add(nebulaMesh);


    // ==========================================
    // 3. PARTICLE WAVE (Foreground)
    // ==========================================
    // White particles with transparency
    const uColor = new THREE.Vector3(1.0, 1.0, 1.0); 

    const particleVertex = `
      attribute float scale;
      uniform float uTime;
      void main() {
        vec3 p = position;
        float s = scale;
        p.y += (sin(p.x + uTime) * 0.5) + (cos(p.y + uTime) * 0.1) * 2.0;
        p.x += (sin(p.y + uTime) * 0.5);
        s += (sin(p.x + uTime) * 0.5) + (cos(p.y + uTime) * 0.1) * 2.0;
        vec4 mvPosition = modelViewMatrix * vec4(p, 1.0);
        gl_PointSize = s * 10.0 * (1.0 / -mvPosition.z);
        gl_Position = projectionMatrix * mvPosition;
      }
    `;

    const particleFragment = `
      uniform vec3 uColor;
      void main() {
        // Calculate distance from center (0.5, 0.5) to create a circle
        float dist = distance(gl_PointCoord, vec2(0.5));
        
        // Smoothly fade the edges (glow effect)
        float alpha = smoothstep(0.5, 0.0, dist);
        
        // Set max opacity to 50% and multiply by the radial fade
        gl_FragColor = vec4(uColor, alpha * 0.50);
      }
    `;

    const gap = 0.3;
    const amountX = 130;
    const amountY = 130;
    const particleNum = amountX * amountY;
    const particlePositions = new Float32Array(particleNum * 3);
    const particleScales = new Float32Array(particleNum);
    
    let i = 0;
    let j = 0;
    for (let ix = 0; ix < amountX; ix++) {
      for (let iy = 0; iy < amountY; iy++) {
        particlePositions[i] = ix * gap - ((amountX * gap) / 2);
        particlePositions[i + 1] = 0;
        particlePositions[i + 2] = iy * gap - ((amountX * gap) / 2);
        particleScales[j] = 1;
        i += 3;
        j++;
      }
    }

    const particleGeometry = new THREE.BufferGeometry();
    particleGeometry.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));
    particleGeometry.setAttribute('scale', new THREE.BufferAttribute(particleScales, 1));

    const particleMaterial = new THREE.ShaderMaterial({
      transparent: true,
      blending: THREE.AdditiveBlending, // Helps it blend nicely with Nebula
      vertexShader: particleVertex,
      fragmentShader: particleFragment,
      uniforms: {
        uTime: { type: 'f', value: 0 },
        uColor: { type: 'v3', value: uColor }
      }
    });

    const particles = new THREE.Points(particleGeometry, particleMaterial);
    scene.add(particles);


    // ==========================================
    // 4. EVENTS & ANIMATION
    // ==========================================
    let targetMouse = new THREE.Vector2();
    let currentMouse = new THREE.Vector2();

    const onResize = () => {
      const w = window.innerWidth;
      const h = window.innerHeight;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
      nebulaUniforms.iResolution.value.set(w, h);
    };

    const onMouseMove = (e) => {
      targetMouse.set(e.clientX, window.innerHeight - e.clientY);
    };

    window.addEventListener("resize", onResize);
    window.addEventListener("mousemove", onMouseMove);
    onResize();

    targetMouse.set(window.innerWidth / 2, window.innerHeight / 2);
    currentMouse.copy(targetMouse);

    const animate = () => {
      requestAnimationFrame(animate);
      
      const time = clock.getElapsedTime();
      
      // Update Nebula
      currentMouse.lerp(targetMouse, 0.03);
      nebulaUniforms.iMouse.value.copy(currentMouse);
      nebulaUniforms.iTime.value = time * 0.6; // Adjusted nebula rotation speed
      
      // Update Particles
      particleMaterial.uniforms.uTime.value += 0.03; // Adjusted particle wave speed
      
      camera.lookAt(scene.position);
      renderer.render(scene, camera);
    };
    animate();
}

// Ensure it runs when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    initBackground();

    // Scroll Reveal Observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal-on-scroll').forEach((el) => {
        observer.observe(el);
    });

    // Make entire cert cards clickable and add hover overlay
    document.querySelectorAll('.cert-card').forEach(card => {
        card.classList.add('cursor-pointer');
        
        // Add magnifying glass overlay to the image container only
        const overlay = document.createElement('div');
        overlay.className = 'absolute inset-0 bg-theme-purple/40 backdrop-blur-[2px] flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-20 pointer-events-none';
        overlay.innerHTML = '<i class="fas fa-search-plus text-4xl text-white drop-shadow-[0_0_15px_rgba(255,255,255,0.8)]"></i>';
        const img = card.querySelector('img');
        if (img && img.parentElement) {
            img.parentElement.appendChild(overlay);
        }

        // Remove inline onclick from image to avoid double firing
        if(img) img.removeAttribute('onclick');

        // Add click listener to the entire card
        card.addEventListener('click', () => {
            if(img) openModal(img.src);
        });
    });
});

// Mobile Menu Logic
document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenuIcon = document.getElementById('mobile-menu-icon');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileLinks = document.querySelectorAll('.mobile-link');
    let isMenuOpen = false;

    function toggleMenu() {
        isMenuOpen = !isMenuOpen;
        if (isMenuOpen) {
            mobileMenu.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-8');
            mobileMenu.classList.add('opacity-100', 'pointer-events-auto', 'translate-y-0');
            mobileMenuIcon.classList.remove('fa-bars');
            mobileMenuIcon.classList.add('fa-times', 'text-theme-cyan');
            document.body.style.overflow = 'hidden'; // prevent background scrolling
        } else {
            mobileMenu.classList.add('opacity-0', 'pointer-events-none', 'translate-y-8');
            mobileMenu.classList.remove('opacity-100', 'pointer-events-auto', 'translate-y-0');
            mobileMenuIcon.classList.add('fa-bars');
            mobileMenuIcon.classList.remove('fa-times', 'text-theme-cyan');
            document.body.style.overflow = '';
        }
    }

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', toggleMenu);
    }

    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (isMenuOpen) toggleMenu();
        });
    });
});
