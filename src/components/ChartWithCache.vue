<script setup>
import { ref, onMounted, watch } from 'vue'
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title, Tooltip, Legend, LineElement,
  CategoryScale, LinearScale, PointElement
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale)

const props = defineProps({
  apiUrl: String,
  cacheKey: String
})

const isLoading = ref(true)
const errorMsg = ref(null)

const colors = [
  'rgb(75, 192, 192)',
  'rgb(255, 99, 132)'
]

const chartData = ref(null)

async function fetchData() {
  isLoading.value = true
  errorMsg.value = null

  try {
    // Vérifie si les données sont en cache
    //const cached = sessionStorage.getItem(props.cacheKey)
    //if (cached) {
    //  const data = JSON.parse(cached)
    //  updateChart(data)
    //  return
    //}

    // Sinon, fait la requête API
    const response = await fetch(props.apiUrl)
    if (!response.ok) throw new Error('Erreur API')
    const data = await response.json()
    sessionStorage.setItem(props.cacheKey, JSON.stringify(data))
    updateChart(data)
  } catch (error) {
    errorMsg.value = error.message
    console.error(`Erreur lors du chargement des données depuis ${props.apiUrl}:`, error)
  } finally {
    isLoading.value = false
  }
}

// Appelé à l’initialisation
onMounted(fetchData)

// Si l’URL ou la clé changent, recharge (au cas où)
watch(
  () => [props.apiUrl, props.cacheKey],
  () => {
    console.log(`Changement détecté pour ${props.cacheKey}, rechargement...`)
    fetchData()
  },
  { immediate: true }
)

function updateChart(data) {
  const labels = data.historical_dates.concat(data.forecast_dates || [])

  const datasets = [
    {
      label: 'Historique',
      data: data.historical,
      borderColor: colors[0],
      fill: false,
      tension: 0.1
    },
    {
      label: 'Prévision',
      data: Array(data.historical.length).fill(null).concat(data.forecast),
      borderColor: colors[1],
      borderDash: [5, 5],
      fill: false,
      tension: 0.1
    }
  ]

  // Crée une copie profonde de `chartData` pour chaque graphique
  chartData.value = {
    labels: [...labels], 
    datasets: [...datasets] // Utilisation de [...datasets] pour un clonage profond
  }
}
</script>

<template>
  <div>
    <Line v-if="chartData" :data="chartData" class="m-8" />
    <p v-else-if="errorMsg" class="text-red-500 mb-4">Erreur : {{ errorMsg }}</p>
    <p v-else class="mb-4">Chargement des données...</p>
  </div>
</template>