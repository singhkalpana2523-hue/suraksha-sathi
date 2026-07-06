import { NavLink, Link } from "react-router-dom";
import ProfileDropdown from "../ProfileDropdown/ProfileDropdown";

function Navbar({ isLoggedIn, setIsLoggedIn }) {
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

        {/* Logo */}

        <div className="flex items-center gap-3">

          <span className="text-3xl">🛡️</span>

          <h1 className="text-2xl font-bold text-cyan-400">
            SurakshaSathi
          </h1>

        </div>

        {/* Navigation Links */}

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

        {/* Authentication */}

        {isLoggedIn ? (

          <ProfileDropdown setIsLoggedIn={setIsLoggedIn} />

        ) : (

          <div className="flex items-center gap-4">

            <Link
              to="/login"
              className="text-white hover:text-cyan-400 transition"
            >
              Login
            </Link>

            <Link
              to="/signup"
              className="bg-cyan-500 hover:bg-cyan-600 text-black font-semibold px-5 py-2 rounded-lg transition"
            >
              Sign Up
            </Link>

          </div>

        )}

      </div>
    </nav>
  );
}

export default Navbar;