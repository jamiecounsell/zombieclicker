function dpsUnlockCtrl(users, api) {
    this.users = users;
    this.api = api.getUnlockables();

    this.unlockableItems = [
            {
                id: "001",
                name: "Fist",
                basePrice: 10,
                baseDamage: 1,
                auto: false,
                imgUrl: "/test.png",
                description: "Five fingers of pain."
            },
            {
                id: "002",
                name: "Wooden Plank",
                basePrice: 20,
                baseDamage: 2,
                auto: false,
                imgUrl: "/test.png",
                description: "Written on the side: Not for killing zombies."
            }
        ];
}

angular.module('zombie').controller('dpsUnlockCtrl', dpsUnlockCtrl)

dpsUnlockCtrl.prototype.upgradeItem = function(itemId) {
    console.log(itemId)
    if (this.users.userGame.unlocks[itemId]) {
        this.users.userGame.unlocks[itemId] ++ ;
    } else  {
        this.users.userGame.unlocks[itemId] = 1;
    }
};

dpsUnlockCtrl.prototype.numberOf = function(itemId) {
    return this.users.userGame.unlocks[itemId] || 0;
};