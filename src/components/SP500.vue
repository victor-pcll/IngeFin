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
    const res = await fetch('http://127.0.0.1:5000/api/predict_SP500')
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
    <h2 class="text-2xl font-bold mb-4">S&P 500 – Analyse et Prévisions</h2>
    <p class="mb-4">
        Le S&amp;P 500, ou Standard &amp; Poor’s 500, est un indice boursier américain qui reflète la performance des 500 plus grandes entreprises cotées en bourse aux États-Unis. Il est considéré comme l’un des meilleurs indicateurs de la santé de l’économie américaine et du marché boursier en général.
    </p>

    <div v-if="chartData" class="bg-white p-4 m-8">
        <Line :data="chartData" />
    </div>
    <div v-else class="text-gray-500 text-sm mb-4">Chargement du graphique...</div>

    <p class="mb-4">
        L’indice a été créé en 1957 par la société Standard &amp; Poor’s, aujourd’hui une division de S&amp;P Global. Contrairement à d’autres indices qui suivent un petit nombre d’entreprises (comme le Dow Jones avec seulement 30 sociétés), le S&amp;P 500 offre une vue d’ensemble plus large du marché, car il comprend des entreprises issues de différents secteurs : technologie, santé, énergie, consommation, finance, etc.
    </p>

    <p class="font-semibold mt-6 mb-2">Caractéristiques principales :</p>
    <ul class="list-disc list-inside mb-4">
        <li><strong>Représentativité :</strong> les 500 entreprises représentent environ 80 % de la capitalisation boursière totale des États-Unis.</li>
        <li><strong>Pondération par capitalisation boursière :</strong> plus une entreprise est grande (en valeur totale de ses actions), plus elle a d’impact sur l’indice. Par exemple, des sociétés comme Apple, Microsoft ou Amazon ont un poids important.</li>
        <li><strong>Diversification :</strong> il couvre un large éventail d’industries, ce qui le rend moins sensible aux variations extrêmes d’un seul secteur.</li>
    </ul>

    <p class="font-semibold mt-6 mb-2">Pourquoi c’est important :</p>
    <ul class="list-disc list-inside mb-4">
        <li>Le S&amp;P 500 est souvent utilisé comme référence (ou « benchmark ») pour comparer la performance des portefeuilles d’investissement.</li>
        <li>Il est aussi utilisé comme base pour des produits financiers comme les fonds indiciels (ETF), qui permettent aux investisseurs de suivre la performance globale du marché américain avec un seul produit.</li>
    </ul>

    <p>
        En résumé, le S&amp;P 500 est un baromètre clé de l’économie américaine et un outil majeur pour les investisseurs du monde entier.
    </p>
</template>