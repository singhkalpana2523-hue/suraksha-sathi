import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

function Login({ setIsLoggedIn }) {

  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!phone || !password) {
      toast.error("Please fill in all fields.");
      return;
    }

    if (!/^[0-9]{10}$/.test(phone)) {
      toast.error("Mobile number must be exactly 10 digits.");
      return;
    }

    // Temporary frontend login
    setIsLoggedIn(true);

    toast.success("Login Successful!");

    navigate("/");
  };

  return (
    <div className="min-h-screen bg-slate-950 flex items-center justify-center px-6">

      <div className="bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl p-10 w-full max-w-md">

        <h1 className="text-4xl font-bold text-white text-center">
          Welcome Back 👋
        </h1>

        <p className="text-slate-400 text-center mt-3">
          Login to continue using SurakshaSathi
        </p>

        <form onSubmit={handleSubmit} className="mt-8">

          {/* Mobile Number */}

          <div className="mb-5">

            <label className="block text-slate-300 mb-2">
              Mobile Number
            </label>

            <div className="flex">

              <span className="bg-slate-800 border border-slate-700 border-r-0 rounded-l-xl px-4 flex items-center text-slate-300">
                +91
              </span>

              <input
                type="tel"
                placeholder="9876543210"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
                maxLength={10}
                className="w-full bg-slate-800 border border-slate-700 rounded-r-xl p-3 text-white focus:outline-none focus:border-cyan-500"
              />

            </div>

          </div>

          {/* Password */}

          <div className="mb-3">

            <label className="block text-slate-300 mb-2">
              Password
            </label>

            <input
              type="password"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl p-3 text-white focus:outline-none focus:border-cyan-500"
            />

          </div>

          {/* Forgot Password */}

          <div className="text-right mb-8">

            <Link
              to="/forgot-password"
              className="text-cyan-400 hover:underline text-sm"
            >
              Forgot Password?
            </Link>

          </div>

          {/* Login Button */}

          <button
            type="submit"
            className="w-full bg-cyan-500 hover:bg-cyan-600 text-black font-semibold py-3 rounded-xl transition"
          >
            Login
          </button>

        </form>

        <p className="text-center text-slate-400 mt-8">

          Don't have an account?{" "}

          <Link
            to="/signup"
            className="text-cyan-400 hover:underline"
          >
            Create Account
          </Link>

        </p>

      </div>

    </div>
  );
}

export default Login;