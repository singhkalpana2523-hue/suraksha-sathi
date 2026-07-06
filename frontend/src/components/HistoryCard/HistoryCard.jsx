import Button from "../Button/Button";
import RiskBadge from "../RiskBadge/RiskBadge";

function HistoryCard({
  type,
  title,
  risk,
  date,
}) {
  return (

    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 hover:border-cyan-500 transition hover:-translate-y-1 transition duration-300">

      <div className="flex justify-between items-start">

        <div>

          <h2 className="text-xl font-bold text-white">

            {type}

          </h2>

          <p className="text-slate-400 mt-2">

            {title}

          </p>

          <p className="text-slate-500 text-sm mt-2">

            {date}

          </p>

        </div>

        <RiskBadge risk={risk} />

      </div>

      <div className="flex gap-4 mt-6">

        <Button>
          View Details
        </Button>

        <button className="bg-red-600 hover:bg-red-700 px-5 py-2 rounded-xl transition">
          Delete
        </button>

      </div>

    </div>

  );
}

export default HistoryCard;