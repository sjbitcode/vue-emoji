<template>
  <div>
    <h1>{{ greeting }}</h1>

    <!-- Image examples
    <img src="./assets/img/u1F60D.png">
    <img v-bind:src="require('./assets/img/u1F60D.png')">
    -->

    <img v-for="name in image_names" v-bind:src="imgUrl(name)">


  </div>

</template>

<script>

export default {
  data () {
    return {
      greeting: 'Hello, there!',

      image_names: [
        'u1F60D',
        'u1F60E',
        'u1F60F'
      ]
    }
  },

  methods: {
    imgUrl: function (name) {
      return require('./assets/img/' + name + '.png');
    }
  }
}
</script>

<style>

</style>
