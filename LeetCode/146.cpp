struct Node {
    Node* prev = nullptr;
    Node* next = nullptr;
    int key;
};

const int MAX_SIZE = 10000;

class LRUCache {
private:
    int vals[MAX_SIZE];
    Node* freqs[MAX_SIZE];
    int capacity;
    int count = 0;
    Node* oldest = nullptr;
    Node* newest = nullptr;

    void refresh(int key){
        if (freqs[key] == newest){
            return;
        }

        // cout << format("Relink the list for {}", key) << endl;
        if (freqs[key]->prev){
            freqs[key]->prev->next = freqs[key]->next;
        }
        if (freqs[key]->next){
            freqs[key]->next->prev = freqs[key]->prev;
        }

        if (freqs[key] == oldest){
            oldest = oldest->prev;
        }

        freqs[key]->prev = nullptr;
        freqs[key]->next = newest;
        newest->prev = freqs[key];
        newest = freqs[key];

        // print();
    }

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        for (int i = 0; i < MAX_SIZE; i++){
            vals[i] = -1;
            freqs[i] = nullptr;
        }
    }
    
    int get(int key) {
        // cout << format("get({})", key) << endl;
        if (vals[key] == -1){
            return -1;
        }

        this->refresh(key);
        return vals[key];
    }
    
    void put(int key, int value) {
        // cout << format("put({},{})", key, value) << endl;
        if (vals[key] != -1){
            // cout << format("Key {} exist, just need to update value", key) << endl;
            vals[key] = value;
            this->refresh(key);
            return;
        }

        if (count == capacity){
            // cout << format("Removing LRU {}", oldest->key) << endl;
            vals[oldest->key] = -1;

            Node* prev = oldest->prev;
            if (prev){
                prev->next = nullptr;
                delete oldest;
                oldest = prev;
            }
        }
        else {
            count++;
        }

        vals[key] = value;
        Node* a = new Node;
        a->key = key;
        a->next = newest;
        if (newest){
            newest->prev = a;
        }
        else {  // count == 0
            oldest = a;
        }
        newest = a;
        if (capacity == 1){
            oldest = a;
        }
        freqs[key] = a;
        // print();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
