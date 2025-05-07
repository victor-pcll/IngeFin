<script setup>
import { ref, onMounted } from 'vue'
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale)

const chartData = ref(null)

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/get_indices')
    if (!response.ok) throw new Error('Erreur API')

    const data = await response.json()
    const { dates, ...indices } = data

    const datasets = Object.entries(indices)
      .filter(([_, values]) => Array.isArray(values) && values.length === dates.length)
      .map(([name, values], i) => ({
        label: name,
        data: values,
        borderColor: ['red', 'blue', 'green', 'orange', 'purple'][i % 5],
        fill: false
      }))

    chartData.value = {
      labels: dates,
      datasets
    }
  } catch (e) {
    console.error(e)
  }
})
</script>

<template>
  <div>
    <h2 class="text-2xl font-bold mb-8">Visualisation des Indices Boursiers</h2>
    <Line v-if="chartData" :data="chartData" />
    <p v-else>Chargement...</p>
  </div>
</template>