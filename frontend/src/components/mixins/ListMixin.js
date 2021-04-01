/*jshint esversion: 6 */

export default {
  mounted() {
    this.fetchItems();
  },
  methods: {
    fetchItems() {
      this.itemsLoading = true;
      this.axios
        .get(this.baseUrl)
        .then(response => {
          this.items = response.data;
          this.itemsLoading = false;
        })
        .catch(error => console.log(error))
    },
    showUpdateDialog(item, event) {
      this.currentItem = item;
      this.$nextTick(() => {
        this.updateDialog = true;
      });
    },
    showDeleteDialog(item, event) {
      this.currentItem = item;
      this.$nextTick(() => {
        this.deleteDialog = true;
      });
    },
    showCreateDialog(event) {
      this.$nextTick(() => {
        this.createDialog = true;
      });
    }
  },
  data() {
    return {
      items: [],
      itemsLoading: true,
      updateDialog: false,
      deleteDialog: false,
      createDialog: false,
      currentItem: null
    }
  }
}
