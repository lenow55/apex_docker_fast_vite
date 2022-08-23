import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'

import App from './App.vue'
import router from './router'

axios.defaults.baseURL = import.meta.env.VITE_API_URL
console.log(import.meta.env.VITE_API_URL)

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
