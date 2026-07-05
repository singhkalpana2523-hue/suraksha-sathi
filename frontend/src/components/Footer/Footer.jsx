import { NavLink } from "react-router-dom";

function Footer() {
  return (
    <footer className="bg-slate-950 border-t border-slate-800 text-white">

      <div className="max-w-7xl mx-auto px-8 py-16">

        <div className="grid md:grid-cols-3 gap-12">

          {/* Brand */}
          <div>
            <h2 className="text-3xl font-bold text-cyan-400">
              🛡️ SurakshaSathi
            </h2>

            <p className="mt-5 text-slate-400 leading-7">
              An AI-powered cybersecurity platform that helps users detect
              phishing messages, fake websites, scam calls, and online fraud
              before they become victims.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-xl font-semibold mb-5 text-white">
              Quick Links
            </h3>

            <div className="flex flex-col gap-3">

              <NavLink to="/" className="text-slate-400 hover:text-cyan-400 transition">
                Home
              </NavLink>

              <NavLink to="/text-analysis" className="text-slate-400 hover:text-cyan-400 transition">
                Text Analysis
              </NavLink>

              <NavLink to="/image-analysis" className="text-slate-400 hover:text-cyan-400 transition">
                Image Analysis
              </NavLink>

              <NavLink to="/voice-analysis" className="text-slate-400 hover:text-cyan-400 transition">
                Voice Analysis
              </NavLink>

              <NavLink to="/history" className="text-slate-400 hover:text-cyan-400 transition">
                History
              </NavLink>

              <NavLink to="/about" className="text-slate-400 hover:text-cyan-400 transition">
                About
              </NavLink>

            </div>
          </div>

          {/* Contact */}
          <div>

            <h3 className="text-xl font-semibold mb-5">
              Contact
            </h3>

            <div className="space-y-3 text-slate-400">

              <p>📧 team@surakshasathi.ai</p>

              <p>🌐 github.com/SurakshaSathi</p>

              <p>💼 LinkedIn</p>

              <p>📍 India</p>

            </div>

          </div>

        </div>

        <div className="border-t border-slate-800 mt-12 pt-8 text-center text-slate-500">

          <p>
            © 2026 <span className="text-cyan-400">SurakshaSathi</span>. All Rights Reserved.
          </p>

          <p className="mt-2">
            Built with ❤️ for a Safer Digital India.
          </p>

        </div>

      </div>

    </footer>
  );
}

export default Footer;