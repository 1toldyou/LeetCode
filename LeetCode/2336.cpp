class SmallestInfiniteSet {
    vector<int> arr;
    vector<bool> exist;
    
    void display() {
        cout << format("n={}\n", arr.size());
        for (int i = 0; i < 10; i++){
            cout << arr[i] << " ";
        }
        cout << endl;
    }

public:
    SmallestInfiniteSet() {
        exist = vector<bool>(1000, true);
        arr = vector<int>(1000);
        for (int i = 0; i < 1000; i++){
            arr[i] = i + 1;
        }

        // display();
    }
    
    int popSmallest() {
        // cout << "popSmallest()\n";
        if (arr.size() < 1){
            return 0;
        }

        int val = arr[0];

        swap(arr.front(), arr.back());
        arr.pop_back();

        int n = arr.size();
        int ptr = 0;
        while(true){
            int left = ptr * 2 + 1;
            int right = ptr * 2 + 2;
            int smallest = ptr;
            if (left < n && arr[left] < arr[smallest]){
                smallest = left;
            } 
            if (right < n && arr[right] < arr[smallest]){
                smallest = right;
            }

            if (smallest != ptr){
                swap(arr[ptr], arr[smallest]);
                ptr = smallest;
            }
            else {
                break;
            }
        }

        // display();
        exist[val-1] = false;
        return val;
    }
    
    void addBack(int num) {
        // cout << format("addBack({})\n", num);
        if (exist[num-1]){
            return;
        }
        exist[num-1] = true;

        arr.emplace_back(num);
        int ptr = arr.size() - 1;
        while (ptr > 0 && arr[(ptr-1)/2] > arr[ptr]){
            swap(arr[ptr], arr[(ptr-1)/2]);
            ptr = (ptr-1)/2;
        }

        // display();
    }
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */
