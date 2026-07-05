import PageHeader from "../../components/PageHeader/PageHeader";

function About() {

  const technologies = [
    "React",
    "Node.js",
    "Express.js",
    "MongoDB",
    "Python",
    "Gemini AI",
    "Tailwind CSS",
    "FAST APIs"
  ];

  return (

    <div className="min-h-screen bg-slate-950 text-white py-16">

      <div className="max-w-6xl mx-auto px-6">

        <PageHeader
          title="About SurakshaSathi"
          subtitle="An AI-powered platform that helps users detect and prevent online scams using Text, Image and Voice analysis."
        />

        {/* Mission */}

        <div className="bg-slate-900 rounded-2xl p-8 border border-slate-800 mb-8">

          <h2 className="text-3xl font-bold text-cyan-400">

            🛡 Our Mission

          </h2>

          <p className="text-slate-300 mt-5 leading-8">

            Our mission is to make the internet safer by helping users
            identify fraudulent messages, suspicious images,
            phishing attempts, fake QR codes and scam voice calls
            before they become victims.

          </p>

        </div>

        {/* About */}

        <div className="bg-slate-900 rounded-2xl p-8 border border-slate-800 mb-8">

          <h2 className="text-3xl font-bold text-cyan-400">

            📖 About the Project

          </h2>

          <p className="text-slate-300 mt-5 leading-8">

            SurakshaSathi combines Artificial Intelligence and
            Cybersecurity to analyze suspicious content using
            Machine Learning and Natural Language Processing.

            It provides users with a risk score, identifies red flags,
            and recommends actions to stay safe online.

          </p>

        </div>

        {/* Technologies */}

        <div className="bg-slate-900 rounded-2xl p-8 border border-slate-800 mb-8">

          <h2 className="text-3xl font-bold text-cyan-400 mb-6">

            ⚙ Technologies Used

          </h2>

          <div className="flex flex-wrap gap-4">

            {technologies.map((tech,index)=>(

              <span
                key={index}
                className="bg-cyan-500/20 text-cyan-300 px-4 py-2 rounded-full"
              >

                {tech}

              </span>

            ))}

          </div>

        </div>

        {/* Team */}

        <div className="bg-slate-900 rounded-2xl p-8 border border-slate-800">

          <h2 className="text-3xl font-bold text-cyan-400">

            👨‍💻 Team

          </h2>

          {/* Team */}

<div className="bg-slate-900 rounded-2xl p-8 border border-slate-800">

  

  <p className="text-slate-400 mt-3">
    SurakshaSathi was built by a team of five members, each contributing to a different part of the project.
  </p>

  <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">

    <div className="bg-slate-800 rounded-xl p-5">
      <h3 className="text-xl font-semibold text-white">
        💻 Frontend Developer
      </h3>
      <p className="text-slate-400 mt-2">
        Built the complete user interface using React, Tailwind CSS and reusable UI components.
      </p>
    </div>

    <div className="bg-slate-800 rounded-xl p-5">
      <h3 className="text-xl font-semibold text-white">
        ⚙️ Backend Developer
      </h3>
      <p className="text-slate-400 mt-2">
        Developed REST APIs, authentication, database integration and server-side logic.
      </p>
    </div>

    <div className="bg-slate-800 rounded-xl p-5">
      <h3 className="text-xl font-semibold text-white">
        🤖 AI Developer
      </h3>
      <p className="text-slate-400 mt-2">
        Integrated AI models for scam detection and intelligent response generation.
      </p>
    </div>

    <div className="bg-slate-800 rounded-xl p-5">
      <h3 className="text-xl font-semibold text-white">
        🧠 Machine Learning Engineer
      </h3>
      <p className="text-slate-400 mt-2">
        Trained and optimized machine learning models for text, image and voice analysis.
      </p>
    </div>

    <div className="bg-slate-800 rounded-xl p-5">
      <h3 className="text-xl font-semibold text-white">
        🎨 UI/UX & Testing
      </h3>
      <p className="text-slate-400 mt-2">
        Designed intuitive user experiences, created prototypes, performed testing and ensured application quality.
      </p>
    </div>

  </div>

</div>

        </div>

      </div>

    </div>

  );

}

export default About;