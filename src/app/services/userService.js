angular.module('zombie').service('userService', function() {
    if (localStorage["userPrefs"]) {
        this.userPrefs = JSON.parse(localStorage["userPrefs"])
    } else {
        this.userPrefs = {}
    }

    if (localStorage["userGame"]) {
        console.log(localStorage["userGame"])
        this.userGame = JSON.parse(localStorage["userGame"])
    } else {
        this.userGame = {
            unlocks: {
                "001": 1
            
            }
        }
    }

    var self = this
    this.saveInterval = setInterval(function() {
        localStorage["userGame"]  = JSON.stringify(self.userGame);
        localStorage["userPrefs"] = JSON.stringify(self.userPrefs);
    }, 1000);
})