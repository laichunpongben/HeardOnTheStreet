/*
A deck with 26 red and 26 black.
Payoff: Red = +1, Black = -1
Can stop any time. 
Find best strategy
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HeardOnTheStreet1_42
{
    class Deck
    {
        private static readonly int startingPlusCards = 26;
        private static readonly int startingMinusCards = 26;
        private static readonly double payoffPlus = 1.0;
        private static readonly double payoffMinus = -1.0;

        private static int remainingPlusCards = startingPlusCards;
        private static int remainingMinusCards = startingMinusCards;
        private static double gamePayoff = 0.0;

        private static double totalPayoff = 0.0;
        private static int stoppingRuleTypeIndex = 0;
        private static int stoppingRuleCaseIndex = 0;
        private static int stoppingRuleSubcaseIndex = 0;

        public Deck()
        {
            ;
        }

        static void Main(string[] args)
        {
            Deck deck = new Deck();
            string result = deck.PlayManyGamesUnderDifferentStoppingRules();
            Console.WriteLine(result);
            Console.Read();
        }

        private double GetUniformRandom()
        {
            Random rnd = new Random(Guid.NewGuid().GetHashCode());
            double u = (double) rnd.Next() / (Int32.MaxValue - 1);
            return u;
        }

        private void DrawACard()
        {
            double dice = GetUniformRandom();
            double fx = (double) remainingPlusCards / (remainingPlusCards + remainingMinusCards);

            bool isDrawPlusCard = (dice < fx);

            if (isDrawPlusCard) {
                remainingPlusCards--;
                gamePayoff += payoffPlus;
            } else {
                remainingMinusCards--;
                gamePayoff += payoffMinus;
            }
        }

        private bool IsDrawNext()
        {
            bool isDrawNext = false;
            int remainingCards = remainingPlusCards + remainingMinusCards;

            switch (stoppingRuleTypeIndex) {
                case 0:
                    if ((gamePayoff <= (double) stoppingRuleCaseIndex) && (remainingPlusCards > stoppingRuleSubcaseIndex) && (remainingCards > 0)) {
                        isDrawNext = true;
                    }
                    break;
                case 1:
                    if ((gamePayoff <= (double) stoppingRuleCaseIndex) && (remainingMinusCards > stoppingRuleSubcaseIndex) && (remainingCards > 0)) {
                        isDrawNext = true;
                    }
                    break;
                case 2:
                    if ((gamePayoff <= (double) stoppingRuleCaseIndex) && (remainingCards > stoppingRuleSubcaseIndex) && (remainingCards > 0)) {
                        isDrawNext = true;
                    }
                    break;
                default:
                    break;
            }

            return isDrawNext;
        }

        private void InitializeDeck()
        {
            remainingPlusCards = startingPlusCards;
            remainingMinusCards = startingMinusCards;
            gamePayoff = 0.0;
        }

        public double PlayGame()
        {
            InitializeDeck();

            while (IsDrawNext()) {
                DrawACard();
            }

            return gamePayoff;
        }

        public double PlayManyGames(int maxGameCount)
        {
            totalPayoff = 0.0;

            for (int i = 0; i < maxGameCount; i++) {
                double payoff = PlayGame();
                totalPayoff += payoff;
            }

            double avgPayoff = (double) totalPayoff / maxGameCount;
            return avgPayoff;
        }

        public string PlayManyGamesUnderDifferentStoppingRules()
        {
            StringBuilder sb = new StringBuilder();
            double result = 0.0;

            for (int i = 0; i < 4; i++) {
                stoppingRuleTypeIndex = i;
                for (int j = 0; j < 5; j++) {
                    stoppingRuleCaseIndex = j;
                    for (int k = 0; k< 26; k++) {
                        stoppingRuleSubcaseIndex = k;
                        result = PlayManyGames(1000);
                        sb.Append("Rule Type ");
                        sb.Append(stoppingRuleTypeIndex.ToString());
                        sb.Append(" Case ");
                        sb.Append(stoppingRuleCaseIndex.ToString());
                        sb.Append(".");
                        sb.Append(stoppingRuleSubcaseIndex.ToString());
                        sb.Append(" : ");
                        sb.AppendLine(result.ToString());
                    }
                    
                }
            }

            string str = sb.ToString();
            return str;
        }
    }
}
