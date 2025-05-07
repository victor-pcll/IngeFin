<script setup>
  import IndicesChart from './components/IndicesChart.vue'
  import Predict from './components/Predict.vue'
  import SNP500 from './components/SP500.vue'
  import CAC40 from './components/CAC40.vue'
  import NASDAQ from './components/NASDAQ.vue'
  import DAX from './components/DAX.vue'
  import NIKKEI from './components/NIKKEI.vue'

  import { ref } from 'vue'

  const activeSection = ref('intro')

  function scrollToSection(id) {
    const el = document.getElementById(id)
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' })
      activeSection.value = id
    }
  }
</script>

<template>
  <div class="flex min-h-screen bg-gray-100">
    <!-- Sidebar -->
    <aside class="w-64 h-screen fixed top-0 left-0 bg-white shadow-md p-6 rounded-lg">
      <h2 class="text-xl font-semibold mb-4 text-blue-600">INDICES</h2>
      <nav class="space-y-2">
        <button
          class="block w-full text-left px-3 py-2 rounded-lg hover:bg-blue-100"
          :class="{ 'bg-blue-200': activeSection === 'S&P 500' }"
          @click="scrollToSection('S&P 500')"
        >
          S&P 500
        </button>
        <button
          class="block w-full text-left px-3 py-2 rounded-lg hover:bg-blue-100"
          :class="{ 'bg-blue-200': activeSection === 'CAC 40' }"
          @click="scrollToSection('CAC 40')"
        >
          CAC 40
        </button>
        <button
          class="block w-full text-left px-3 py-2 rounded-lg hover:bg-blue-100"
          :class="{ 'bg-blue-200': activeSection === 'NASDAQ' }"
          @click="scrollToSection('NASDAQ')"
        >
          NASDAQ
        </button>
        <button
          class="block w-full text-left px-3 py-2 rounded-lg hover:bg-blue-100"
          :class="{ 'bg-blue-200': activeSection === 'DAX' }"
          @click="scrollToSection('DAX')"
        >
          DAX
        </button>
        <button
          class="block w-full text-left px-3 py-2 rounded-lg hover:bg-blue-100"
          :class="{ 'bg-blue-200': activeSection === 'NIKKEI' }"
          @click="scrollToSection('NIKKEI')"
        >
          NIKKEI
        </button>
      </nav>
    </aside>

    <!-- Content -->
    <main class="ml-64 flex-1 p-10 space-y-16">
      <section id="intro" class="bg-white p-8 rounded-xl shadow">
        <IndicesChart />
      </section>

      <section id="chart" class="bg-white p-8 rounded-xl shadow">
        <Predict />
      </section>

      <section id="S&P 500" class="bg-white p-8 rounded-xl shadow">
        <SNP500 />
      </section>

      <section id="CAC 40" class="bg-white p-8 rounded-xl shadow">
        <CAC40 />
      </section>

      <section id="NASDAQ" class="bg-white p-8 rounded-xl shadow">
        <NASDAQ />
      </section>

      <section id="DAX" class="bg-white p-8 rounded-xl shadow">
        <DAX />
      </section>

      <section id="NIKKEI" class="bg-white p-8 rounded-xl shadow">
        <NIKKEI />
      </section>
    </main>
  </div>
</template>