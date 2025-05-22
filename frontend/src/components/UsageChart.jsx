import { Pie } from "react-chartjs-2";

const UsageChart = ({ data }) => {
  const chartData = {
    labels: Object.keys(data),
    datasets: [{
      data: Object.values(data),
      backgroundColor: ['#3b82f6', '#ef4444', '#facc15', '#10b981'],
    }]
  };

  return <Pie data={chartData} />;
};
