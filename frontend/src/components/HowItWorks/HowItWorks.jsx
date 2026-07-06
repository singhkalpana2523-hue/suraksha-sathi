import { FileText, BrainCircuit, SearchCheck, ShieldCheck } from "lucide-react";
import { motion } from "framer-motion";

const steps = [
  {
    icon: FileText,
    title: "1. Upload",
    desc: "Paste text or upload an image/voice recording.",
  },
  {
    icon: BrainCircuit,
    title: "2. AI Analysis",
    desc: "Gemini AI understands the scam content.",
  },
  {
    icon: SearchCheck,
    title: "3. Knowledge Search",
    desc: "Relevant scam examples are retrieved using RAG.",
  },
  {
    icon: ShieldCheck,
    title: "4. Get Result",
    desc: "Receive risk score, scam type and recommendations.",
  },
];

function HowItWorks() {
  return (
    <section className="bg-slate-900 py-28 text-white">
      <div className="max-w-7xl mx-auto px-8">

        <h2 className="text-5xl font-bold text-center">
          How It
          <span className="text-cyan-400"> Works</span>
        </h2>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mt-20">

          {steps.map((step, index) => {

            const Icon = step.icon;

            return (

              <motion.div
                key={index}
                whileHover={{ y: -10 }}
                className="rounded-2xl bg-slate-800 p-8 text-center border border-slate-700"
              >

                <Icon
                  className="mx-auto text-cyan-400"
                  size={50}
                />

                <h3 className="text-2xl font-bold mt-6">

                  {step.title}

                </h3>

                <p className="text-slate-400 mt-4">

                  {step.desc}

                </p>

              </motion.div>

            );

          })}

        </div>

      </div>
    </section>
  );
}

export default HowItWorks;