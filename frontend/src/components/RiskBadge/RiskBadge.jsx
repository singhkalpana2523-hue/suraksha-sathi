function RiskBadge({ risk }) {

  let bgColor = "";
  let textColor = "";

  switch (risk) {
    case "High":
      bgColor = "bg-red-500/20";
      textColor = "text-red-400";
      break;

    case "Medium":
      bgColor = "bg-yellow-500/20";
      textColor = "text-yellow-400";
      break;

    default:
      bgColor = "bg-green-500/20";
      textColor = "text-green-400";
  }

  return (
    <span
      className={`${bgColor} ${textColor} px-3 py-1 rounded-full font-semibold text-sm`}
    >
      {risk} Risk
    </span>
  );
}

export default RiskBadge;