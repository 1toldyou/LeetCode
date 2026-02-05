class Solution {
public:
    string simplifyPath(string path) {
        stack<string> paths;
        string currentDir = "";
        for (int i = 1; i < path.size(); i++){
            if (path[i] == '/'){
                if (currentDir.size() > 0){ // means path[i-1] != '/'
                    if (currentDir == ".."){
                        if (paths.size() > 0){
                            paths.pop();
                        }
                    }
                    else if (currentDir != ".") {
                        paths.push(currentDir);    
                        // cout << format("pushed {}\n", currentDir);                 
                    }
                    currentDir = "";
                }
            }
            else {
                currentDir += path[i];
            }
        }

        // in case the input path didn't end with "/"
        if (currentDir.size() > 0){ // means path[i-1] != '/'
            if (currentDir == ".."){
                if (paths.size() > 0){
                    paths.pop();
                }
            }
            else if (currentDir != ".") {
                paths.push(currentDir);                     
            }
            currentDir = "";
        }

        string result;
        while (paths.size() > 0){
            result = "/" + paths.top() + result;
            paths.pop();
        }

        if (result.size() == 0){
            result = "/";
        }

        return result;
    }
};
