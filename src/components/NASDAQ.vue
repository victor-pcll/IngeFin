<script setup>
import ChartWithCache from './ChartWithCache.vue'
</script>

<template>
    <h2 class="text-2xl font-bold mb-4">NASDAQ</h2>
    <p class="mb-4">
      Le <strong>NASDAQ</strong> (National Association of Securities Dealers Automated Quotations) est un indice boursier américain qui regroupe principalement des entreprises de <strong>technologie et d'innovation</strong>. Il est souvent vu comme un baromètre des secteurs de la technologie, des biotechnologies et des entreprises à forte croissance.
    </p>

    <ChartWithCache api-url="http://127.0.0.1:5000/api/predict_NASDAQ" cache-key="'nasdaqData'"/>

    <p class="mb-4">
      Créé en <strong>1971</strong>, le NASDAQ a été le premier marché boursier électronique, ce qui en fait un acteur clé dans la transition vers une bourse numérique. Contrairement à d’autres indices comme le S&amp;P 500 ou le Dow Jones, le NASDAQ est davantage orienté vers les entreprises à forte croissance, avec une forte représentation du secteur technologique, notamment des géants comme <strong>Apple</strong>, <strong>Microsoft</strong>, <strong>Amazon</strong> et <strong>Alphabet (Google)</strong>.
    </p>
    
    <p class="font-semibold mt-6 mb-2">Caractéristiques principales :</p>
    <ul class="list-disc list-inside mb-4">
      <li><strong>Technologie et croissance :</strong> le NASDAQ est dominé par des entreprises du secteur technologique et des entreprises en forte croissance, comme des startups et des sociétés de biotechnologie.</li>
      <li><strong>Composé principalement d’actions technologiques :</strong> des entreprises comme <strong>Apple</strong>, <strong>Microsoft</strong>, <strong>Facebook</strong>, et <strong>Amazon</strong> ont un poids très important dans l’indice.</li>
      <li><strong>Marché électronique :</strong> Le NASDAQ a été le premier marché boursier entièrement électronique, ce qui en fait un pionnier dans le domaine des transactions numériques.</li>
    </ul>

    <p class="font-semibold mt-6 mb-2">Pourquoi c’est important :</p>
    <ul class="list-disc list-inside mb-4">
      <li>Le NASDAQ est souvent utilisé comme un **indicateur clé** pour suivre la performance du secteur technologique et des entreprises innovantes.</li>
      <li>Il est également utilisé pour créer des produits financiers comme les **ETF NASDAQ** qui permettent aux investisseurs de suivre l’évolution des actions technologiques.</li>
    </ul>

    <p>
      En résumé, le NASDAQ est un indice **indispensable pour suivre l’évolution des technologies de pointe** et des entreprises à croissance rapide, offrant aux investisseurs un aperçu précieux du secteur technologique mondial.
    </p>
</template>