<template>
  <div>
    <app-header v-bind:title="title"></app-header>
    <app-emoji v-bind:emojis="emojis"></app-emoji>
    <app-footer></app-footer>
  </div>

</template>

<script>

import Emojis from './sample'

import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import Emoji from './components/Emoji.vue'

export default {
  components: {
    'app-header': Header,
    'app-footer': Footer,
    'app-emoji': Emoji
  },

  data () {
    return {
      title: 'Emoji Index',
      emojis: Emojis
    }
  },

  methods: {
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
