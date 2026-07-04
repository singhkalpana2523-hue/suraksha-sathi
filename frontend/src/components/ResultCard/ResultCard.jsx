function ResultCard({
  risk,
  score,
  category,
  confidence,
  redFlags,
  recommendations,
}) {

  const riskColor =
    risk === "High"
      ? "text-red-400"
      : risk === "Medium"
      ? "text-yellow-400"
      : "text-green-400";

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-8 mt-10">

      <h2 className="text-3xl font-bold text-cyan-400">
        AI Analysis Result
      </h2>

      <div className="grid md:grid-cols-4 gap-6 mt-8">

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-gray-400">Risk Level</p>

          <h3 className={`text-2xl font-bold mt-2 ${riskColor}`}>
            {risk}
          </h3>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-gray-400">Risk Score</p>

          <h3 className="text-2xl font-bold mt-2">
            {score}/10
          </h3>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-gray-400">Category</p>

          <h3 className="text-xl font-bold mt-2">
            {category}
          </h3>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-gray-400">Confidence</p>

          <h3 className="text-xl font-bold mt-2">
            {confidence}
          </h3>
        </div>

      </div>

      <div className="mt-10">

        <h3 className="text-2xl font-bold text-yellow-400">
          🚩 Red Flags
        </h3>

        <ul className="list-disc list-inside mt-5 space-y-2 text-gray-300">

          {redFlags.map((flag, index) => (
            <li key={index}>{flag}</li>
          ))}

        </ul>

      </div>

      <div className="mt-10">

        <h3 className="text-2xl font-bold text-green-400">
          🛡 Recommended Actions
        </h3>

        <ul className="list-disc list-inside mt-5 space-y-2 text-gray-300">

          {recommendations.map((item, index) => (
            <li key={index}>{item}</li>
          ))}

        </ul>

      </div>

    </div>
  );
}

export default ResultCard;