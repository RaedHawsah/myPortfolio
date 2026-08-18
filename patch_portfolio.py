import re

with open('/home/rexkov/Documents/myPortfolio/index.html', 'r') as f:
    content = f.read()

# 1. Replace Skills Section
skills_start_marker = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 relative z-20">'
skills_end_marker = '        </div>\n    </section>\n\n    <!-- Projects Section -->'

skills_new = '''<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-6 relative z-20">
            <!-- Skill 1: Offensive Security -->
            <div class="glass-card rounded-2xl p-6 hover:-translate-y-2 transition-transform duration-300 group border border-gray-800 hover:border-theme-cyan hover:shadow-[0_0_30px_rgba(0,229,255,0.4)]">
                <div class="w-14 h-14 rounded-full bg-black/60 border border-theme-cyan/60 flex items-center justify-center mb-5 shadow-[0_0_20px_rgba(0,229,255,0.3)] group-hover:shadow-[0_0_40px_rgba(0,229,255,0.6)] transition-all">
                    <i class="fas fa-biohazard text-theme-cyan text-xl"></i>
                </div>
                <h3 class="text-xl font-bold text-white mb-3">Offensive Security & Pwn</h3>
                <p class="text-gray-400 text-sm leading-relaxed">
                    eJPT Certified, Network & Web Pentesting, Binary Exploitation, Metasploit, Burp Suite.
                </p>
            </div>

            <!-- Skill 2: Reverse Engineering -->
            <div class="glass-card rounded-2xl p-6 hover:-translate-y-2 transition-transform duration-300 group border border-gray-800 hover:border-theme-purple hover:shadow-[0_0_30px_rgba(168,85,247,0.4)]">
                <div class="w-14 h-14 rounded-full bg-black/60 border border-theme-purple/60 flex items-center justify-center mb-5 shadow-[0_0_20px_rgba(168,85,247,0.3)] group-hover:shadow-[0_0_40px_rgba(168,85,247,0.6)] transition-all">
                    <i class="fas fa-bug text-theme-purple text-xl"></i>
                </div>
                <h3 class="text-xl font-bold text-white mb-3">Reverse Engineering & Low-Level</h3>
                <p class="text-gray-400 text-sm leading-relaxed">
                    Malware Analysis, x86/x64 Assembly, Memory Corruption, Ghidra, IDA Pro.
                </p>
            </div>

            <!-- Skill 3: AI & Cyber-Physical Security -->
            <div class="glass-card rounded-2xl p-6 hover:-translate-y-2 transition-transform duration-300 group border border-gray-800 hover:border-theme-orange hover:shadow-[0_0_30px_rgba(255,107,0,0.4)]">
                <div class="w-14 h-14 rounded-full bg-black/60 border border-theme-orange/60 flex items-center justify-center mb-5 shadow-[0_0_20px_rgba(255,107,0,0.3)] group-hover:shadow-[0_0_40px_rgba(255,107,0,0.6)] transition-all">
                    <i class="fas fa-brain text-theme-orange text-xl"></i>
                </div>
                <h3 class="text-xl font-bold text-white mb-3">AI & Cyber-Physical Security</h3>
                <p class="text-gray-400 text-sm leading-relaxed">
                    Medical IoT (IoMT) Security, Anomaly Detection Algorithms (Isolation Forest), Deep Learning.
                </p>
            </div>

            <!-- Skill 4: Enterprise & Cloud Architecture -->
            <div class="glass-card rounded-2xl p-6 hover:-translate-y-2 transition-transform duration-300 group border border-gray-800 hover:border-blue-500 hover:shadow-[0_0_30px_rgba(59,130,246,0.4)]">
                <div class="w-14 h-14 rounded-full bg-black/60 border border-blue-500/60 flex items-center justify-center mb-5 shadow-[0_0_20px_rgba(59,130,246,0.3)] group-hover:shadow-[0_0_40px_rgba(59,130,246,0.6)] transition-all">
                    <i class="fas fa-network-wired text-blue-500 text-xl"></i>
                </div>
                <h3 class="text-xl font-bold text-white mb-3">Enterprise & Cloud Architecture</h3>
                <p class="text-gray-400 text-sm leading-relaxed">
                    Secure Cloud Infrastructure (AWS), Enterprise Systems (SAP S/4HANA), Python & C/C++ Scripting.
                </p>
            </div>'''

idx_skills_start = content.find(skills_start_marker)
idx_skills_end = content.find(skills_end_marker)

if idx_skills_start != -1 and idx_skills_end != -1:
    content = content[:idx_skills_start] + skills_new + '\n' + content[idx_skills_end:]
else:
    print("Could not find skills section markers")


# 2. Replace Achievements Section
achievements_start_marker = '            <!-- Browser-like Tabs -->'
achievements_end_marker = '        </div>\n    </section>\n\n    <!-- Footer / Contact -->'

achievements_new = '''        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6" id="certs-container">
            <!-- Achievement 1 -->
            <div class="glass-card rounded-xl p-6 md:p-8 border border-gray-800 hover:border-yellow-500 hover:shadow-[0_0_30px_rgba(234,179,8,0.3)] transition-all duration-500 group flex items-center gap-6 relative overflow-hidden md:col-span-2">
                <div class="absolute inset-0 bg-gradient-to-r from-yellow-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="w-16 h-16 shrink-0 rounded-full bg-black/80 border border-yellow-500/50 flex items-center justify-center shadow-[0_0_15px_rgba(234,179,8,0.4)] group-hover:scale-110 transition-transform duration-500 relative z-10">
                    <i class="fas fa-trophy text-yellow-500 text-2xl group-hover:animate-pulse"></i>
                </div>
                <div class="flex-grow relative z-10">
                    <h4 class="text-white font-bold text-xl md:text-2xl mb-1 group-hover:text-yellow-400 transition-colors">Guinness World Record Holder</h4>
                    <p class="text-gray-400 text-sm md:text-base">Largest AI video lesson (Achieved with Kanz & Ministry of HR)</p>
                </div>
            </div>

            <!-- Achievement 2 -->
            <div class="glass-card rounded-xl p-6 md:p-8 border border-gray-800 hover:border-red-500 hover:shadow-[0_0_30px_rgba(239,68,68,0.3)] transition-all duration-500 group flex items-center gap-6 relative overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-r from-red-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="w-16 h-16 shrink-0 rounded-full bg-black/80 border border-red-500/50 flex items-center justify-center shadow-[0_0_15px_rgba(239,68,68,0.4)] group-hover:scale-110 transition-transform duration-500 relative z-10">
                    <i class="fas fa-user-secret text-red-500 text-2xl group-hover:animate-pulse"></i>
                </div>
                <div class="flex-grow relative z-10">
                    <h4 class="text-white font-bold text-xl md:text-2xl mb-1 group-hover:text-red-400 transition-colors">eJPT (Junior Penetration Tester)</h4>
                    <p class="text-gray-400 text-sm md:text-base">INE Security</p>
                </div>
            </div>

            <!-- Achievement 3 -->
            <div class="glass-card rounded-xl p-6 md:p-8 border border-gray-800 hover:border-theme-cyan hover:shadow-[0_0_30px_rgba(0,229,255,0.3)] transition-all duration-500 group flex items-center gap-6 relative overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-r from-theme-cyan/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="w-16 h-16 shrink-0 rounded-full bg-black/80 border border-theme-cyan/50 flex items-center justify-center shadow-[0_0_15px_rgba(0,229,255,0.4)] group-hover:scale-110 transition-transform duration-500 relative z-10">
                    <i class="fas fa-shield-alt text-theme-cyan text-2xl group-hover:animate-pulse"></i>
                </div>
                <div class="flex-grow relative z-10">
                    <h4 class="text-white font-bold text-xl md:text-2xl mb-1 group-hover:text-theme-cyan transition-colors">Advanced Cybersecurity Certs</h4>
                    <p class="text-gray-400 text-sm md:text-base">Malware Analysis & eCDFP (Netriders), IBM Cybersecurity Fundamentals</p>
                </div>
            </div>

            <!-- Achievement 4 -->
            <div class="glass-card rounded-xl p-6 md:p-8 border border-gray-800 hover:border-orange-500 hover:shadow-[0_0_30px_rgba(249,115,22,0.3)] transition-all duration-500 group flex items-center gap-6 relative overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-r from-orange-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="w-16 h-16 shrink-0 rounded-full bg-black/80 border border-orange-500/50 flex items-center justify-center shadow-[0_0_15px_rgba(249,115,22,0.4)] group-hover:scale-110 transition-transform duration-500 relative z-10">
                    <i class="fab fa-aws text-orange-500 text-2xl group-hover:animate-pulse"></i>
                </div>
                <div class="flex-grow relative z-10">
                    <h4 class="text-white font-bold text-xl md:text-2xl mb-1 group-hover:text-orange-400 transition-colors">AWS Certified Cloud Practitioner</h4>
                    <p class="text-gray-400 text-sm md:text-base">Amazon Web Services</p>
                </div>
            </div>

            <!-- Achievement 5 -->
            <div class="glass-card rounded-xl p-6 md:p-8 border border-gray-800 hover:border-blue-500 hover:shadow-[0_0_30px_rgba(59,130,246,0.3)] transition-all duration-500 group flex items-center gap-6 relative overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-r from-blue-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="w-16 h-16 shrink-0 rounded-full bg-black/80 border border-blue-500/50 flex items-center justify-center shadow-[0_0_15px_rgba(59,130,246,0.4)] group-hover:scale-110 transition-transform duration-500 relative z-10">
                    <i class="fas fa-server text-blue-500 text-2xl group-hover:animate-pulse"></i>
                </div>
                <div class="flex-grow relative z-10">
                    <h4 class="text-white font-bold text-xl md:text-2xl mb-1 group-hover:text-blue-400 transition-colors">ERP with SAP S/4HANA (TS410)</h4>
                    <p class="text-gray-400 text-sm md:text-base">Brandenburg University, Germany</p>
                </div>
            </div>'''

idx_ach_start = content.find(achievements_start_marker)
idx_ach_end = content.find(achievements_end_marker)

if idx_ach_start != -1 and idx_ach_end != -1:
    content = content[:idx_ach_start] + achievements_new + '\n' + content[idx_ach_end:]
else:
    print("Could not find achievements section markers")


with open('/home/rexkov/Documents/myPortfolio/index.html', 'w') as f:
    f.write(content)

print("HTML replaced successfully.")
