<script setup>
import { ref, onMounted } from 'vue'
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement } from 'chart.js'

// Enregistrement des composants nécessaires pour Chart.js
ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale)

// Données du graphique
const chartData = ref({
  labels: [],
  datasets: []
})

// Palette de couleurs pour les courbes
const colors = [
  'rgb(75, 192, 192)',
  'rgb(255, 99, 132)',
  'rgb(54, 162, 235)',
  'rgb(255, 206, 86)',
  'rgb(153, 102, 255)'
]

onMounted(async () => {
  try {
    // Vérifie si les données sont déjà en cache
    const cached = sessionStorage.getItem('indicesData')
    if (cached) {
      const data = JSON.parse(cached)
      updateIndicesChart(data)
      return
    }

    // Sinon, appelle l’API
    const response = await fetch('http://127.0.0.1:5000/api/get_indices')
    if (!response.ok) throw new Error("Erreur API")
    const data = await response.json()

    // Cache les données
    sessionStorage.setItem('indicesData', JSON.stringify(data))

    updateIndicesChart(data)

  } catch (error) {
    console.error('Erreur lors de la récupération des indices:', error)
  }
})

function updateIndicesChart(data) {
  const firstKey = Object.keys(data)[0]
  const length = data[firstKey]?.length || 0
  const labels = Array.from({ length }, (_, i) => `Jour ${i + 1}`)

  const datasets = Object.entries(data).map(([name, values], i) => ({
    label: `${name} - Clôture`,
    data: values,
    fill: false,
    borderColor: colors[i % colors.length],
    tension: 0.1,
    pointRadius: 4,
    pointBackgroundColor: colors[i % colors.length],
    pointBorderColor: '#fff',
    pointBorderWidth: 1
  }))

  chartData.value = {
    labels,
    datasets
  }
}
</script>

<template>
  <div class="p-4">
    <h2 class="text-2xl font-bold mb-4">Visualisation des Indices Boursiers</h2>
    <Line class="m-8" v-if="chartData.datasets.length > 0" :data="chartData"/>
    <p v-else class="mb-4">Chargement des données...</p>
  </div>
</template>