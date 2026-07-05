import { Brain, ScanText, Mic, ShieldCheck } from "lucide-react";
import { motion } from "framer-motion";

const features = [
  {
    icon: Brain,
    title: "AI Scam Detection",
    description:
      "Advanced AI detects phishing, UPI fraud and social engineering scams."
  },
  {
    icon: ScanText,
    title: "OCR Analysis",
    description:
      "Upload screenshots and let AI extract and inspect suspicious text."
  },
  {
    icon: Mic,
    title: "Voice Intelligence",
    description:
      "Analyze suspicious calls and voice recordings using AI."
  },
  {
    icon: ShieldCheck,
    title: "Knowledge Base",
    description:
      "Powered by RAG using verified cybercrime awareness datasets."
  }
];

function Features() {
  return (
    <section className="bg-slate-900 text-white py-24">

      <div className="max-w-7xl mx-auto px-8">

        <motion.h2
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: .6 }}
          className="text-5xl font-bold text-center"
        >
          Why Choose
          <span className="text-cyan-400">
            {" "}SurakshaSathi
          </span>
        </motion.h2>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mt-20">

          {features.map((feature, index) => {

            const Icon = feature.icon;

            return (

              <motion.div

                key={index}

                whileHover={{
                  y: -10,
                  scale: 1.03
                }}

                className="bg-slate-800 rounded-2xl p-8 border border-slate-700 hover:border-cyan-400 transition cursor-pointer"

              >

                <Icon
                  size={45}
                  className="text-cyan-400"
                />

                <h3 className="text-2xl font-bold mt-6">

                  {feature.title}

                </h3>

                <p className="text-slate-300 mt-4 leading-7">

                  {feature.description}

                </p>

              </motion.div>

            );

          })}

        </div>

      </div>

    </section>
  );
}

export default Features;