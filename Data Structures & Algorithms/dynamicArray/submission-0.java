class DynamicArray {
    int[] container;
    int size;

    public DynamicArray(int capacity) {
        container = new int[capacity];
        size = 0;
    }

    public int get(int i) {
        return container[i];
    }

    public void set(int i, int n) {
        container[i] = n;
    }

    public void pushback(int n) {
        if(size == container.length){
            resize();
        }

        container[size] = n;
        size++;
    }

    public int popback() {
        size--;
        return container[size];
    }

    private void resize() {
        int[] temp = new int[container.length * 2];
        for(int i = 0; i < container.length; i++){
            temp[i] = container[i];
        }
        container = temp;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return container.length;
    }
}
