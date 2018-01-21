import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
    {
        title: 'Ma ville',
        icon: 'nb-home',
        link: '/pages/dashboard',
        home: true,
    },
    {
        title: 'Garderie',
        icon: 'ion-ios-people',
        children: [
            {
                title: 'Rechercher une garderie',
                link: '/pages/daycare',
            },
            {
                title: 'Mes garderies',
                link: '/pages/daycare/my',
            }
        ],
    },
    {
        title: 'Activités sportives',
        icon: 'ion-ios-basketball',
        children: [
            {
                title: 'Rechercher une activité',
                link: '/pages/sports',
            },
            {
                title: 'Mes inscriptions',
                link: '/pages/sports/my',
            }
        ],
    },
    {
        title: 'Services de garde',
        icon: 'ion-university',
        children: [
            {
                title: 'Rechercher',
                link: '/auth/login',
            },
            {
                title: 'Mes inscriptions',
                link: '/auth/register',
            }
        ],
    },
    {
        title: 'Règlages',
        icon: 'ion-gear-b',
        children: [
            {
                title: 'Gérer mes paiements',
                link: '/auth/login',
            }
        ],
    },
];
