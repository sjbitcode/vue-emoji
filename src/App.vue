<template>
  <div>

    <p style="font-size:5rem;width:100%;">{{ emoji }}</p>




  </div>

</template>

<script>

import Emojis from './sorted_emojis'

console.log(Emojis);

export default {
  data () {
    return {
      emoji: '\ud83d\ude00'
    }
  },

  methods: {

    copy: function() {
      this.$clipboard('');
    }
  }
}
</script>

<style>
h1 {
  padding: 10px;
  border: 2px solid black;
  width: 100px;
  background-color: #ffe;
}
</style>
