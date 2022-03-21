<template lang="pug">
  .container(:class="{'single': coffee === 'Stille'}")
    h1.header {{ coffee }}

    v-stepper.item(v-model="position" vertical v-if="coffee !== 'Stille'")
      template(v-for="(step, index) in steps")
        v-stepper-step(
          :key="`${step}-step`"
          :complete="position > index + 1"
          :step="index + 1"
        ) {{ steps[index] }}

        v-stepper-content(:step="step" v-if="index+1 !== steps.length" )

</template>

<script>
const coffee_types = {
  'Stille': {
    label: 'Stille'
  },
  'Hot_Water': {
    label: 'Heißes Wasser',
    steps: ['Hochdruckpumpe', 'Wasserausgabe']
  },
  'Warme_Milch': {
    label: 'Warme Milch',
    steps: ['Milch_aufheizen', 'Milch erwärmen']

  },
  'Easy_Clean': {
    label: 'Reinigungsprogramm',
    steps:  ['Ausgangsdüse spülen', 'Dampfreinigung der Ausgangsdüse', 'Reinigung der Milchschaumdüse']
  },
  'Milchschaum': {
    label: 'Milchschaum',
    steps: ['Milch aufheizen', 'Milchschaum']
  },
  'Cafe_Creme': {
    label: 'Café Creme',
    steps: ['Einlass Kaffeebohnen', 'Mahlprozess', 'Mahlwerk ausblasen', 'Mechanik Brüheinheit', 'Tampen', 'Präinfusion Brühprozess', 'Brühprozess', 'Auswurf Kaffeepuck']
  },
  'Latte_macchiato': {
    label: 'Latte Macchiato',
    steps: ['Milchschaum', 'Einlass Kaffeebohnen', 'Mahlprozess', 'Mahlwerk ausblasen', 'Mechanik Bruüheinheit', 'Tampen', 'Wassereinleitung Thermoblock', 'Präinfusion Brühprozess', 'Brühprozess', 'Auswurf Kaffeepuck']
  },
  'Cappuccino': {
    label: 'Cappuccino',
    steps: ['Einlass Kaffeebohnen', 'Mahlprozess', 'Mahlwerk ausblasen', 'Mechanik Brüheinheit', 'Tampen', 'Präinfusion Brühprozess', 'Brühprozess', 'Milch aufheizen', 'Auswurf Kaffeepuck', 'Milchschaum']
  },
  'Espresso': {
    label: 'Espresso',
    steps: ['Einlass Kaffeebohnen', 'Mahlprozess', 'Mahlwerkausblasen', 'Mechanik Brüheinheit', 'Tampen', 'Präinfusion Brühprozess', 'Brühprozess', 'Auswurf Kaffeepuck']
  }
}
export default {
  data() {
    return {
      position: parseInt(this.$route.query.position),
      coffeeType: this.$route.query.coffeetype
    };
  },
  computed: {
    steps () {
      return coffee_types[this.coffeeType].steps
    },
    coffee () {
      console.log(this.coffeeType)
      return coffee_types[this.coffeeType].label
    }
  }
};
</script>

<style scoped lang="sass">
.image
  justify-content: center
  width: 27.5rem
  margin-top: 2rem
  margin-block-end: 30px

.header
  font-size: 5rem

.container
  height: 100vh
  display: flex
  align-items: center
  justify-content: space-between
  &.single
    justify-content: center

  .item
    width: 50%

.v-stepper--vertical
  padding-bottom: 1em
</style>
