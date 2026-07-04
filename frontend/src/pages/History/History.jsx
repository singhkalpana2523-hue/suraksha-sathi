import PageHeader from "../../components/PageHeader/PageHeader";
import HistoryCard from "../../components/HistoryCard/HistoryCard";

function History() {

  const history = [

    {
      type: "📝 Text Analysis",
      title: "Suspicious bank message",
      risk: "High",
      date: "Today",
    },

    {
      type: "🖼 Image Analysis",
      title: "invoice.jpg",
      risk: "Medium",
      date: "Yesterday",
    },

    {
      type: "🎤 Voice Analysis",
      title: "call_recording.mp3",
      risk: "Low",
      date: "2 Days Ago",
    },

  ];

  return (

    <div className="min-h-screen bg-slate-950 text-white py-16">

      <div className="max-w-5xl mx-auto px-6">

        <PageHeader
          title="Analysis History"
          subtitle="View all your previous AI scam analyses."
        />
        <div className="bg-slate-900 rounded-xl p-5 border border-slate-800 mb-8">

    <h2 className="text-xl font-semibold">

        Total Analyses

    </h2>

    <p className="text-4xl font-bold text-cyan-400 mt-3">

        {history.length}

    </p>

</div>
        <div className="mb-8">

  <input

    type="text"

    placeholder="Search previous analyses..."

    className="w-full p-4 rounded-xl bg-slate-900 border border-slate-700 text-white focus:outline-none focus:border-cyan-500"

  />

</div>
<div className="flex gap-4 mb-8 flex-wrap">

  <button className="bg-cyan-500 px-4 py-2 rounded-lg">
    All
  </button>

  <button className="bg-slate-800 px-4 py-2 rounded-lg">
    Text
  </button>

  <button className="bg-slate-800 px-4 py-2 rounded-lg">
    Image
  </button>

  <button className="bg-slate-800 px-4 py-2 rounded-lg">
    Voice
  </button>

</div>

        <div className="space-y-6">

          {history.map((item, index) => (

            <HistoryCard
              key={index}
              type={item.type}
              title={item.title}
              risk={item.risk}
              date={item.date}
            />

          ))}

        </div>

      </div>

    </div>

  );

}

export default History;