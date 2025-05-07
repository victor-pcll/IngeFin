<script setup>
import { useRoute } from 'vue-router'
</script>

<template>
  <div class="flex min-h-screen bg-white">
    <!-- Sidebar -->
    <aside class="w-64 h-screen fixed top-0 left-0 bg-gray-100 shadow-md p-6 rounded-lg">
      <h2 class="text-xl font-semibold mb-4 text-blue-600">M.F.A.</h2>
      <nav class="space-y-2">
        <router-link
          to="/"
          class="block w-full text-left px-3 py-2 rounded-lg hover:bg-blue-100"
          :class="{ 'bg-blue-200': $route.path === '/' }"
        >
          Indices
        </router-link>
        <router-link
          to="/sp500"
          class="block w-full text-left px-3 py-2 rounded-lg hover:bg-blue-100"
          :class="{ 'bg-blue-200': $route.path === '/sp500' }"
        >
          S&P 500
        </router-link>
        <router-link
          to="/cac40"
          class="block w-full text-left px-3 py-2 rounded-lg hover:bg-blue-100"
          :class="{ 'bg-blue-200': $route.path === '/cac40' }"
        >
          CAC 40
        </router-link>
        <router-link
          to="/nasdaq"
          class="block w-full text-left px-3 py-2 rounded-lg hover:bg-blue-100"
          :class="{ 'bg-blue-200': $route.path === '/nasdaq' }"
        >
          NASDAQ
        </router-link>
        <router-link
          to="/dax"
          class="block w-full text-left px-3 py-2 rounded-lg hover:bg-blue-100"
          :class="{ 'bg-blue-200': $route.path === '/dax' }"
        >
          DAX
        </router-link>
        <router-link
          to="/nikkei"
          class="block w-full text-left px-3 py-2 rounded-lg hover:bg-blue-100"
          :class="{ 'bg-blue-200': $route.path === '/nikkei' }"
        >
          NIKKEI
        </router-link>
      </nav>
    </aside>

    <!-- Content -->
    <main class="ml-64 flex-1 p-10 space-y-16">
      <router-view />
    </main>
  </div>
</template>