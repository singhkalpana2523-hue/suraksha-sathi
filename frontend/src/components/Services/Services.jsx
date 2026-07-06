import { FileText, Image, Mic, History } from "lucide-react";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";

function Services() {
  const navigate = useNavigate();

  const services = [
    {
      title: "Text Analysis",
      description: "Analyze suspicious SMS, Emails and WhatsApp messages.",
      icon: FileText,
      route: "/text-analysis",
      color: "text-cyan-400",
    },
    {
      title: "Image Analysis",
      description: "Upload screenshots for OCR + AI scam detection.",
      icon: Image,
      route: "/image-analysis",
      color: "text-green-400",
    },
    {
      title: "Voice Analysis",
      description: "Upload voice recordings and detect scam calls.",
      icon: Mic,
      route: "/voice-analysis",
      color: "text-purple-400",
    },
    {
      title: "History",
      description: "View previous analyses and AI reports.",
      icon: History,
      route: "/history",
      color: "text-orange-400",
    },
  ];

  return (
    <section
  id="services"
  className="bg-slate-950 py-24 text-white"
>

      <div className="max-w-7xl mx-auto px-8">

        <h2 className="text-5xl font-bold text-center">
          Analyze
          <span className="text-cyan-400"> Anything</span>
        </h2>

        <p className="text-center text-slate-400 mt-5 text-lg">
          Choose what you want SurakshaSathi AI to analyze.
        </p>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mt-16">

          {services.map((service, index) => {

            const Icon = service.icon;

            return (

              <motion.div
                key={index}
                whileHover={{
                  scale: 1.05,
                  y: -10,
                }}
                onClick={() => navigate(service.route)}
                className="cursor-pointer rounded-2xl bg-slate-900 border border-slate-700 hover:border-cyan-400 p-8 transition"
              >

                <Icon
                  size={50}
                  className={service.color}
                />

                <h3 className="text-2xl font-bold mt-6">

                  {service.title}

                </h3>

                <p className="text-slate-400 mt-4 leading-7">

                  {service.description}

                </p>

              </motion.div>

            );

          })}

        </div>

      </div>

    </section>
  );
}

export default Services;