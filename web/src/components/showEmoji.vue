<template>
    <div class="container is-fluid"> 
        <div class="columns is-multiline is-mobile">
            <div v-for="emoji in emojis">

                <b-tooltip v-bind:label="formatShortcode(emoji.shortcode)">

                    <div class="column" v-on:click="copy(emoji.shortcode)" v-bind:ref="'emoji_' + emoji.shortcode">

                        <div class="emoji">
                            <a class="grow shake-freeze" v-bind:class="getRandomStyle()" v-on:click="copiedToast">
                                {{ emoji.surrogate_pairs | format-code }}
                            </a>
                        </div>
                    </div>

                </b-tooltip>
            </div>
        </div>
    </div>
</template>

<script>
    import _ from 'lodash';

    export default {
        props: {
            emojis: {
                type: Array,
                required: true
            }
        },

        data() {
            return {
                css_shake_classes: [
                    'shake',
                    'shake-hard',
                    'shake-slow',
                    'shake-little',
                    'shake-horizontal',
                    'shake-vertical',
                    'shake-rotate',
                    'shake-chunk'
                ]
            }
        },

        methods: {
            copy: function(shortcode) {
              // Find ref and copy to clipboard
              var ref_name = 'emoji_' + shortcode;
              this.$clipboard(this.$refs[ref_name][0].innerText);
            },

            formatShortcode: function(str) {
                return ':' + str + ':'
            },

            getRandomStyle: function() {
               return _.shuffle(this.css_shake_classes)[0]; 
            },

            copiedToast() {
                this.$toast.open('Copied!')
            },
        }
    }
</script>

<style scoped>
.emoji {
    font-size: 6em;
    margin: 0 30px;
}

@keyframes grow {
  0% {
      transform: scale(1.5);
  }
  50% {
      transform: scale(.95);
  }
  100% {
      transform: scale(1.5);
  }
}

@keyframes floatup {
    20% {opacity: .999;}
    100% {
        -webkit-transform:translate3d(0,-80%,0);
        transform:translate3d(0,-80%,0);
    }
}

.emoji:active a {
    animation: grow 1.2s 1 ease-out !important;
}
</style>