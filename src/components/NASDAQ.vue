]<script setup>
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

const chartDataCAC = ref(null)

async function fetchCACData() {
  try {
    // Vérifie si les données sont déjà dans le cache
    const cached = sessionStorage.getItem("cacData")
    if (cached) {
      const dataCAC = JSON.parse(cached)
      updateChartData(dataCAC)
      return
    }

    // Sinon, appel à l'API
    const res = await fetch('http://127.0.0.1:5000/api/predict_CAC40')
    if (!res.ok) throw new Error("Erreur API")
    const dataCAC = await res.json()
    console.log(dataCAC) // Log the data to verify the structure

    // Cache les données dans sessionStorage
    sessionStorage.setItem("cacData", JSON.stringify(dataCAC))

    updateChartData(dataCAC)

  } catch (e) {
    console.error("Erreur lors du chargement des données :", e)
  }
}

function updateChartData(data) {
  chartDataCAC.value = {
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
  fetchCACData()
})
</script>

<template>
  <h2 class="text-2xl font-bold mb-4">CAC 40 – Analyse et Prévisions</h2>
  <p class="mb-4">
    Le <strong>CAC 40</strong>, ou <strong>Cotation Assistée en Continu 40</strong>, est un indice boursier français qui reflète la performance des <strong>40 plus grandes entreprises cotées à la Bourse de Paris</strong>. Il est souvent considéré comme l’indicateur principal de la santé de l’économie française et du marché boursier européen.
  </p>

  <div v-if="chartDataCAC" class="bg-white p-4 m-8">
    <Line :data="chartDataCAC" />
  </div>
  <div v-else class="text-gray-500 text-sm mb-4">Chargement du graphique...</div>

  <!-- Description of CAC 40 -->
  <p class="mb-4">
    L’indice a été créé en <strong>1987</strong> par la société Euronext, et il inclut des entreprises issues de <strong>divers secteurs</strong> tels que la technologie, l’énergie, les biens de consommation, la finance, et bien d’autres. Il est pondéré en fonction de la capitalisation boursière des entreprises, ce qui signifie que les plus grandes entreprises, en termes de valeur, ont un impact plus important sur l’évolution de l’indice.
  </p>
  
  <p class="font-semibold mt-6 mb-2">Caractéristiques principales :</p>
  <ul class="list-disc list-inside mb-4">
    <li><strong>Représentativité :</strong> les 40 entreprises représentent une grande part de la capitalisation boursière totale de la France et incluent des entreprises de secteurs clés de l'économie.</li>
    <li><strong>Pondération par capitalisation boursière :</strong> plus une entreprise est grande (en valeur totale de ses actions), plus elle influence l’indice. Par exemple, des sociétés comme <strong>L'Oréal</strong>, <strong>TotalEnergies</strong>, ou <strong>Sanofi</strong> ont un poids majeur dans l'indice.</li>
    <li><strong>Diversification :</strong> bien qu'il soit limité à 40 entreprises, le CAC 40 couvre une large gamme de secteurs, ce qui permet de mieux représenter l'économie française.</li>
  </ul>

  <p class="font-semibold mt-6 mb-2">Pourquoi c’est important :</p>
  <ul class="list-disc list-inside mb-4">
    <li>Le CAC 40 est souvent utilisé comme <strong>référence</strong> pour comparer la performance des portefeuilles d’investissement en France et en Europe.</li>
    <li>Il est également utilisé comme base pour des produits financiers comme les fonds indiciels (ETF), permettant aux investisseurs de suivre la performance du marché français à travers un seul produit.</li>
  </ul>

  <p>
    En résumé, le CAC 40 est un <strong>baromètre essentiel de l’économie française</strong> et un <strong>outil de référence pour les investisseurs</strong> en Europe.
  </p>
</template>