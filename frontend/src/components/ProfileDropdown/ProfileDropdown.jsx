import { useState, useRef, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";

function ProfileDropdown({ setIsLoggedIn }) {
  const [open, setOpen] = useState(false);

  const dropdownRef = useRef(null);
  const navigate = useNavigate();

  const user = {
    name: "Aniket Sharma",
    phone: "+91 9876543210",
  };

  // Close dropdown when clicking outside
  useEffect(() => {
    function handleClickOutside(event) {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target)
      ) {
        setOpen(false);
      }
    }

    document.addEventListener("mousedown", handleClickOutside);

    return () =>
      document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  // Get initials
  const initials = user.name
    .split(" ")
    .map((word) => word[0])
    .join("");

  const handleLogout = () => {
    setIsLoggedIn(false);
    setOpen(false);
    navigate("/login");
  };

  return (
    <div className="relative" ref={dropdownRef}>
      {/* Avatar Button */}

      <button
        onClick={() => setOpen(!open)}
        className="flex items-center gap-3 bg-slate-800 hover:bg-slate-700 px-4 py-2 rounded-xl transition"
      >
        <div className="w-10 h-10 rounded-full bg-cyan-500 text-black font-bold flex items-center justify-center">
          {initials}
        </div>

        <div className="hidden md:flex flex-col items-start">
          <span className="text-white font-medium">
            {user.name.split(" ")[0]}
          </span>

          <span className="text-xs text-slate-400">
            Logged In
          </span>
        </div>

        <span
          className={`text-white transition-transform duration-300 ${
            open ? "rotate-180" : ""
          }`}
        >
          ▼
        </span>
      </button>

      {/* Dropdown */}

      {open && (
        <div className="absolute right-0 mt-4 w-72 rounded-2xl bg-slate-900 border border-slate-700 shadow-2xl overflow-hidden animate-fade">

          <div className="p-5 border-b border-slate-700">

            <div className="flex items-center gap-4">

              <div className="w-14 h-14 rounded-full bg-cyan-500 text-black font-bold flex items-center justify-center text-xl">
                {initials}
              </div>

              <div>

                <h2 className="text-white font-semibold">
                  {user.name}
                </h2>

                <p className="text-slate-400 text-sm">
                  {user.phone}
                </p>

              </div>

            </div>

          </div>

          <Link
            to="/profile"
            className="block px-5 py-3 text-slate-300 hover:bg-slate-800 transition"
            onClick={() => setOpen(false)}
          >
            👤 My Profile
          </Link>

          <Link
            to="/history"
            className="block px-5 py-3 text-slate-300 hover:bg-slate-800 transition"
            onClick={() => setOpen(false)}
          >
            📜 History
          </Link>

          <button
            onClick={handleLogout}
            className="w-full text-left px-5 py-3 text-red-400 hover:bg-slate-800 transition"
          >
            🚪 Logout
          </button>

        </div>
      )}
    </div>
  );
}

export default ProfileDropdown;