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

async function fetchSnPData() {
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

onMounted(() => {
  fetchSnPData()
})
</script>

<template>
    <h2 class="text-2xl font-bold mb-4">DAX – Analyse et Prévisions</h2>
    <p class="mb-4">
      Le <strong>DAX</strong>, ou <strong>Deutscher Aktienindex</strong>, est un indice boursier allemand qui reflète la performance des <strong>30 plus grandes entreprises cotées à la Bourse de Francfort</strong>. Il est souvent considéré comme l’indicateur principal de la santé de l’économie allemande et de l’ensemble du marché boursier européen.
    </p>

    <div v-if="chartData" class="bg-white p-4 m-8">
        <Line :data="chartData" />
    </div>
    <div v-else class="text-gray-500 text-sm mb-4">Chargement du graphique...</div>

    <p class="mb-4">
      Le DAX a été créé en <strong>1988</strong> par la Bourse de Francfort (aujourd’hui part de la société Deutsche Börse). L’indice est pondéré par capitalisation boursière, ce qui signifie que les entreprises ayant une plus grande valeur boursière influencent davantage son évolution. Le DAX couvre des entreprises issues de divers secteurs comme la technologie, l’automobile, l’énergie, les biens de consommation et la finance.
    </p>
    
    <p class="font-semibold mt-6 mb-2">Caractéristiques principales :</p>
    <ul class="list-disc list-inside mb-4">
      <li><strong>Représentativité :</strong> les 30 entreprises représentent une large portion de la capitalisation boursière allemande et incluent des géants de l’industrie comme <strong>Volkswagen</strong>, <strong>Siemens</strong>, et <strong>Allianz</strong>.</li>
      <li><strong>Pondération par capitalisation boursière :</strong> comme pour d'autres indices majeurs, les grandes entreprises ont un impact plus important sur l’indice. Par exemple, <strong>BMW</strong> et <strong>Deutsche Bank</strong> pèsent lourdement dans le DAX.</li>
      <li><strong>Diversification :</strong> bien que l’indice soit limité à 30 entreprises, il couvre un éventail assez large de secteurs économiques, ce qui permet de mieux refléter l’économie allemande dans son ensemble.</li>
    </ul>

    <p class="font-semibold mt-6 mb-2">Pourquoi c’est important :</p>
    <ul class="list-disc list-inside mb-4">
      <li>Le DAX est utilisé comme un **indicateur clé** de la performance de l’économie allemande et permet aux investisseurs de suivre les entreprises majeures du pays.</li>
      <li>Il est également la base pour de nombreux produits financiers, comme les **ETF DAX**, permettant aux investisseurs de suivre la performance du marché allemand avec un seul produit.</li>
    </ul>

    <p>
      En résumé, le DAX est un **baromètre essentiel de l’économie allemande** et de l’industrie européenne, offrant un outil puissant pour les investisseurs cherchant à comprendre l’évolution du marché boursier en Allemagne.
    </p>
</template>