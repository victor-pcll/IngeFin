<script setup>
import { ref, onMounted } from 'vue'
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Title,
  Legend,
} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(LineElement, PointElement, LinearScale, CategoryScale, Title, Legend)

const chartData = ref(null)
const chartOptions = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top'
    },
    title: {
      display: true,
      text: 'S&P 500: Historique et Prévision (ARIMA)',
    },
  },
}

async function fetchData() {
  try {
    // Vérifie si les données sont déjà dans le cache
    const cached = sessionStorage.getItem("snpData")
    if (cached) {
      const data = JSON.parse(cached)
      updateChartData(data)
      return
    }

    // Sinon, appel à l'API
    const res = await fetch('http://127.0.0.1:5000/api/predict')
    if (!res.ok) throw new Error("Erreur API")
    const data = await res.json()

    // Cache les données dans sessionStorage
    sessionStorage.setItem("snpData", JSON.stringify(data))

    updateChartData(data)

  } catch (e) {
    console.error("Erreur lors du chargement des données :", e)
  }
}

function updateChartData(data) {
  chartData.value = {
    labels: [...data.historical_dates, ...data.forecast_dates],
    datasets: [
      {
        label: 'Historique',
        data: [...data.historical, ...Array(data.forecast.length).fill(null)],
        borderColor: 'blue',
        tension: 0.3,
      },
      {
        label: 'Prévision',
        data: [...Array(data.historical.length).fill(null), ...data.forecast],
        borderColor: 'orange',
        borderDash: [5, 5],
        tension: 0.3,
      }
    ]
  }
}

onMounted(fetchData)
</script>

<template>
  <div class="p-4">
    <h2 class="text-2xl font-bold mb-4">Predictions des Indices Boursiers</h2>
    <div class="m-8" v-if="chartData">
        <Line :data="chartData" />
    </div>
    <p v-else class="mb-4">Chargement des données...</p>
  </div>
</template>