import Hero from "../../components/Hero/Hero";
import Features from "../../components/Features/Features";
import Services from "../../components/Services/Services";
import HowItWorks from "../../components/HowItWorks/HowItWorks";
import Footer from "../../components/Footer/Footer";

function Home() {
  return (
    <div className="bg-slate-950">
      <Hero />
      <Features />
      <Services />
      <HowItWorks />
      <Footer />
    </div>
  );
}

export default Home;