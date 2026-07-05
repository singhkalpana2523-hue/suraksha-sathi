function PageHeader({ title, subtitle }) {
  return (
    <div className="text-center mb-12">

      <h1 className="text-5xl md:text-6xl font-bold text-white">

        {title}

      </h1>

      <p className="text-slate-400 text-lg mt-5 max-w-3xl mx-auto">

        {subtitle}

      </p>

    </div>
  );
}

export default PageHeader;
