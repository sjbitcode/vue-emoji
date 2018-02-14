<template>
  <div>

    <!-- Image examples
    <img src="./assets/img/u1F60D.png">
    <img v-bind:src="require('./assets/img/u1F60D.png')">
    <img v-bind:src="require(`${path}`)">
    -->

    <img v-for="name in image_names" v-bind:src="imgUrl(name)">

    <div>
      <h1 @click="copy">{{ greeting }}</h1>
    </div>

    <p style="font-size:5rem;width:100%;">&#x1F354</p>
    
    <p style="font-size:5rem;width:100%;">&#x1F486;&#x1F3FB;&#x200D;&#x2640;&#xFE0F;</p>
    
    <p style="font-size:5rem;width:100%;">&#x1F3CC;&#x1F3FF;&#x0200D;&#x02640;&#x0FE0F;</p>


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
    },

    copy: function() {
      // this.$clipboard(String.fromCodePoint(0x1F354));
      this.$clipboard(String.fromCodePoint(0x1F486,0x1F3FB,0x200D,0x2640,0xFE0F));
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
