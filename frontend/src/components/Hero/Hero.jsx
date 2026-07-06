import { motion } from "framer-motion";

function Hero() {
  return (
    <section className="min-h-[90vh] flex items-center bg-slate-950 text-white">

      <div className="max-w-7xl mx-auto px-8 grid lg:grid-cols-2 gap-10 items-center">

        {/* Left */}

        <motion.div
          initial={{ opacity: 0, x: -80 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8 }}
        >

          <p className="text-cyan-400 uppercase tracking-[5px] font-semibold">
            AI Powered Cyber Security
          </p>

          <h1 className="text-6xl font-extrabold leading-tight mt-5">

            Protect Yourself

            <br />

            <span className="text-cyan-400">
              From Digital Scams
            </span>

          </h1>

          <p className="text-slate-300 text-xl mt-8 leading-9 max-w-xl">

            Analyze suspicious text messages,
            emails,
            screenshots,
            WhatsApp chats,
            and voice recordings
            using AI + OCR + Voice Intelligence.

          </p>

          <div className="flex gap-5 mt-10">

            <button className="bg-cyan-500 hover:bg-cyan-600 px-8 py-4 rounded-xl font-semibold transition">

              Analyze Now

            </button>

            <button className="border border-cyan-500 px-8 py-4 rounded-xl hover:bg-cyan-500 transition">

              Learn More

            </button>

          </div>

        </motion.div>

        {/* Right */}

        <motion.div

          initial={{ opacity: 0, x: 80 }}

          animate={{ opacity: 1, x: 0 }}

          transition={{ duration: 1 }}

          className="flex justify-center"

        >

          <div className="w-96 h-96 rounded-full bg-cyan-500/20 flex items-center justify-center shadow-[0_0_120px_20px_rgba(6,182,212,0.35)]">

            <span className="text-[180px]">
              🛡️
            </span>

          </div>

        </motion.div>

      </div>

    </section>
  );
}

export default Hero;