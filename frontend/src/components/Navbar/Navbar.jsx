import { NavLink } from "react-router-dom";

function Navbar() {
  const links = [
    { name: "Home", path: "/" },
    { name: "Text", path: "/text-analysis" },
    { name: "Image", path: "/image-analysis" },
    { name: "Voice", path: "/voice-analysis" },
    { name: "History", path: "/history" },
    { name: "About", path: "/about" },
  ];

  return (
    <nav className="sticky top-0 z-50 backdrop-blur-md bg-slate-900/80 border-b border-slate-700">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-8 py-4">

        <div className="flex items-center gap-3">
          <span className="text-3xl">🛡️</span>

          <h1 className="text-2xl font-bold text-cyan-400">
            SurakshaSathi
          </h1>
        </div>

        <div className="flex gap-8 text-white">

          {links.map((link) => (

            <NavLink
              key={link.name}
              to={link.path}
              className={({ isActive }) =>
                `transition duration-300 ${
                  isActive
                    ? "text-cyan-400 font-semibold"
                    : "hover:text-cyan-400"
                }`
              }
            >
              {link.name}
            </NavLink>

          ))}

        </div>

      </div>
    </nav>
  );
}

export default Navbar;