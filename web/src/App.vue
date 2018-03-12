<template>
  <div>
    <app-header></app-header>
    <router-view></router-view>
    <app-footer></app-footer>
  </div>

</template>

<script>

import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

export default {
  components: {
    'app-header': Header,
    'app-footer': Footer
  }
}
</script>

<style scoped>
h1 {
  padding: 10px;
  border: 2px solid black;
  width: 100px;
  background-color: #ffe;
}
</style>
