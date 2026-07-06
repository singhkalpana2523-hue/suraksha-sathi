import { useState } from "react";
import { Link } from "react-router-dom";
import toast from "react-hot-toast";

function Signup() {

  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [agree, setAgree] = useState(false);

  const handleSubmit = (e) => {

    e.preventDefault();

    if (!name || !phone || !password || !confirmPassword) {
      toast.error("Please fill in all fields.");
      return;
    }

    if (!/^[A-Za-z ]+$/.test(name)) {
      toast.error("Name should contain only letters.");
      return;
    }

    if (!/^[0-9]{10}$/.test(phone)) {
      toast.error("Mobile number must be exactly 10 digits.");
      return;
    }

    if (
      !/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$/.test(password)
    ) {
      toast.error(
        "Password must be at least 8 characters and include uppercase, lowercase, number and special character."
      );
      return;
    }

    if (password !== confirmPassword) {
      toast.error("Passwords do not match.");
      return;
    }

    if (!agree) {
      toast.error("Please accept the Terms & Conditions.");
      return;
    }

    toast.success("Account Created Successfully!");
  };

  return (
    <div className="min-h-screen bg-slate-950 flex items-center justify-center px-6 py-12">

      <div className="bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl p-10 w-full max-w-md">

        <h1 className="text-4xl font-bold text-white text-center">
          Create Account
        </h1>

        <p className="text-slate-400 text-center mt-3">
          Join SurakshaSathi and stay protected from online scams.
        </p>

        <form onSubmit={handleSubmit} className="mt-8">

          <div className="mb-5">

            <label className="block text-slate-300 mb-2">
              Full Name
            </label>

            <input
              type="text"
              placeholder="Enter your full name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl p-3 text-white focus:outline-none focus:border-cyan-500"
            />

          </div>

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

          <div className="mb-5">

            <label className="block text-slate-300 mb-2">
              Password
            </label>

            <input
              type="password"
              placeholder="Create a password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl p-3 text-white focus:outline-none focus:border-cyan-500"
            />

          </div>

          <div className="mb-5">

            <label className="block text-slate-300 mb-2">
              Confirm Password
            </label>

            <input
              type="password"
              placeholder="Confirm your password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl p-3 text-white focus:outline-none focus:border-cyan-500"
            />

          </div>

          <div className="flex items-start gap-3 mb-8">

            <input
              type="checkbox"
              checked={agree}
              onChange={(e) => setAgree(e.target.checked)}
              className="mt-1 accent-cyan-500"
            />

            <label className="text-sm text-slate-400">
              I agree to the{" "}
              <span className="text-cyan-400 hover:underline cursor-pointer">
                Terms & Conditions
              </span>{" "}
              and{" "}
              <span className="text-cyan-400 hover:underline cursor-pointer">
                Privacy Policy
              </span>.
            </label>

          </div>

          <button
            type="submit"
            className="w-full bg-cyan-500 hover:bg-cyan-600 text-black font-semibold py-3 rounded-xl transition"
          >
            Create Account
          </button>

        </form>

        <p className="text-center text-slate-400 mt-8">

          Already have an account?{" "}

          <Link
            to="/login"
            className="text-cyan-400 hover:underline"
          >
            Login
          </Link>

        </p>

      </div>

    </div>
  );
}

export default Signup;