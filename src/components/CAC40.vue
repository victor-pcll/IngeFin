<script setup>
import ChartWithCache from './ChartWithCache.vue'
</script>

<template>
  <h2 class="text-2xl font-bold mb-4">CAC 40</h2>
  <p class="mb-4">
    Le <strong>CAC 40</strong>, ou <strong>Cotation Assistée en Continu 40</strong>, est un indice boursier français qui reflète la performance des <strong>40 plus grandes entreprises cotées à la Bourse de Paris</strong>. Il est souvent considéré comme l’indicateur principal de la santé de l’économie française et du marché boursier européen.
  </p>

  <ChartWithCache api-url="http://127.0.0.1:5000/api/predict_CAC40" cache-key="'cacData'"/>

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