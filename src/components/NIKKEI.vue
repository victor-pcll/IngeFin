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
  PointElement,
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)

const chartData = ref(null)

async function fetchNikkeiData() {
  try {
    // Vérifie si les données sont déjà dans le cache
    const cached = sessionStorage.getItem("nikkeiData")
    if (cached) {
      const data = JSON.parse(cached)
      updateChartData(data)
      return
    }

    // Sinon, appel à l'API
    const res = await fetch('http://127.0.0.1:5000/api/predict_nikkei') // Change the endpoint to match the Nikkei data API
    if (!res.ok) throw new Error("Erreur API")
    const data = await res.json()

    // Cache les données dans sessionStorage
    sessionStorage.setItem("nikkeiData", JSON.stringify(data))

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

onMounted(() => {
  fetchNikkeiData()
})
</script>

<template>
    <h2 class="text-2xl font-bold mb-4">Nikkei 225 – Analyse et Prévisions</h2>
    <p class="mb-4">
      Le <strong>Nikkei 225</strong> est un indice boursier japonais qui suit la performance des <strong>225 plus grandes entreprises cotées à la Bourse de Tokyo</strong>. Il est l’un des indices boursiers les plus suivis en Asie et représente un indicateur clé de l’économie japonaise.
    </p>

    <div v-if="chartData" class="bg-white p-4 m-8">
        <Line :data="chartData" />
    </div>
    <div v-else class="text-gray-500 text-sm mb-4">Chargement du graphique...</div>

    <p class="mb-4">
      Créé en <strong>1950</strong>, le Nikkei 225 reflète la performance de diverses entreprises japonaises, allant de l’industrie automobile à la haute technologie. L’indice est calculé sur une base de prix (et non de capitalisation boursière), ce qui signifie que les sociétés avec des actions ayant un prix plus élevé influencent davantage l’indice, indépendamment de leur taille de capitalisation boursière.
    </p>
    
    <p class="font-semibold mt-6 mb-2">Caractéristiques principales :</p>
    <ul class="list-disc list-inside mb-4">
      <li><strong>Représentativité :</strong> les 225 entreprises couvrent de nombreux secteurs comme l’automobile, l’électronique, la finance, et l’énergie, avec des géants comme <strong>Toyota</strong>, <strong>Sony</strong>, et <strong>Honda</strong>.</li>
      <li><strong>Indice basé sur les prix :</strong> contrairement à d’autres indices comme le S&P 500, le Nikkei 225 est calculé en fonction des prix des actions et non de la capitalisation boursière.</li>
      <li><strong>Orientation sectorielle :</strong> bien que le Nikkei soit un indice diversifié, il est particulièrement influencé par les grandes entreprises japonaises des secteurs technologiques et industriels.</li>
    </ul>

    <p class="font-semibold mt-6 mb-2">Pourquoi c’est important :</p>
    <ul class="list-disc list-inside mb-4">
      <li>Le Nikkei 225 est un baromètre essentiel de l’économie japonaise, permettant aux investisseurs de suivre la performance des entreprises japonaises et d’évaluer la santé économique du pays.</li>
      <li>Il est également utilisé pour créer des produits financiers comme les ETF Nikkei, offrant ainsi une opportunité d'investir dans l'économie japonaise avec un seul produit.</li>
    </ul>

    <p>
      En résumé, le Nikkei 225 est un indice clé pour comprendre l’évolution de l’économie japonaise et suivre la performance des plus grandes entreprises du pays. C’est un outil essentiel pour les investisseurs cherchant à se positionner sur le marché asiatique.
    </p>
</template>