import { createRouter, createWebHistory } from 'vue-router'
import IndicesChart from './components/IndicesChart.vue'
import SNP500 from './components/SP500.vue'
import CAC40 from './components/CAC40.vue'
import NASDAQ from './components/NASDAQ.vue'
import DAX from './components/DAX.vue'
import NIKKEI from './components/NIKKEI.vue'

const routes = [
  { path: '/', component: IndicesChart, name: 'intro' },
  { path: '/sp500', component: SNP500, name: 'sp500' },
  { path: '/cac40', component: CAC40, name: 'cac40' },
  { path: '/nasdaq', component: NASDAQ, name: 'nasdaq' },
  { path: '/dax', component: DAX, name: 'dax' },
  { path: '/nikkei', component: NIKKEI, name: 'nikkei' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router