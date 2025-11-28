# =============================================================================
# FILENAME: lord_bridegroom_philadelphia_ecosystem.py
# DESCRIPTION: 大费城汽车广告生态系统模拟 - VP级战略分析工具
# CREATOR: LORD BRIDEGROOM - 商业战略数据科学家
# =============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')

print("🚀 LORD BRIDEGROOM 生态系统模拟器初始化中...")

class QualityScoreOptimizer:
    """质量得分优化引擎 - 将商业洞察量化为算法优势"""
    
    def __init__(self):
        self.components = {
            'landing_page': {
                'page_speed': 0.25, 'mobile_friendly': 0.20,
                'conversion_forms': 0.15, 'trust_signals': 0.10
            },
            'ad_relevance': {
                'keyword_match': 0.30, 'ad_copy_quality': 0.25, 
                'ad_extensions': 0.15
            },
            'expected_ctr': {
                'historical_ctr': 0.40, 'industry_benchmark': 0.20,
                'competitor_gap': 0.10
            }
        }
    
    def calculate_quality_score(self, dealer_data):
        total_score = 0
        lp_score = (
            dealer_data['page_speed'] * self.components['landing_page']['page_speed'] +
            dealer_data['mobile_friendly'] * self.components['landing_page']['mobile_friendly'] +
            dealer_data['conversion_forms'] * self.components['landing_page']['conversion_forms'] +
            dealer_data['trust_signals'] * self.components['landing_page']['trust_signals']
        ) * 4
        ar_score = (
            dealer_data['keyword_match'] * self.components['ad_relevance']['keyword_match'] +
            dealer_data['ad_copy_quality'] * self.components['ad_relevance']['ad_copy_quality'] +
            dealer_data['ad_extensions'] * self.components['ad_relevance']['ad_extensions']
        ) * 3.5
        ectr_score = (
            dealer_data['historical_ctr'] * self.components['expected_ctr']['historical_ctr'] +
            dealer_data['industry_benchmark'] * self.components['expected_ctr']['industry_benchmark'] +
            dealer_data['competitor_gap'] * self.components['expected_ctr']['competitor_gap']
        ) * 2.5
        total_score = lp_score + ar_score + ectr_score
        return min(total_score, 10.0)

class PhiladelphiaAutoAdPlatform:
    """大费城汽车广告生态系统模拟平台"""
    
    def __init__(self):
        self.dealers = []
        self.auction_history = []
        self.quality_optimizer = QualityScoreOptimizer()
        
    def add_dealer(self, dealer_data):
        dealer_data['remaining_budget'] = dealer_data['daily_budget']
        dealer_data['total_impressions'] = 0
        dealer_data['total_clicks'] = 0
        dealer_data['total_conversions'] = 0
        dealer_data['total_spent'] = 0
        
        if 'quality_score' not in dealer_data:
            dealer_data['quality_score'] = self.quality_optimizer.calculate_quality_score(dealer_data)
            
        self.dealers.append(dealer_data)
        print(f"✅ 已添加: {dealer_data['name']} | 质量得分: {dealer_data['quality_score']:.1f}")

    def simulate_search_auction(self, search_query, user_location, user_income_tier):
        active_dealers = [d for d in self.dealers if d['remaining_budget'] > 0.1]
        if not active_dealers:
            return None
            
        auction_data = []
        for dealer in active_dealers:
            base_ad_rank = dealer['max_bid'] * dealer['quality_score']
            location_match = 1.2 if user_location in dealer['target_locations'] else 1.0
            income_match = 1.3 if (user_income_tier == 'high' and dealer['inventory_focus'] == 'luxury') else 1.0
            adjusted_ad_rank = base_ad_rank * location_match * income_match
            
            auction_data.append({
                'dealer': dealer,
                'ad_rank': adjusted_ad_rank,
                'base_ad_rank': base_ad_rank
            })
        
        auction_data.sort(key=lambda x: x['ad_rank'], reverse=True)
        
        if auction_data:
            winner_data = auction_data[0]
            winner = winner_data['dealer']
            winner_ad_rank = winner_data['ad_rank']
            
            if len(auction_data) > 1:
                second_ad_rank = auction_data[1]['base_ad_rank']
                actual_cpc = (second_ad_rank / winner['quality_score']) + 0.01
            else:
                actual_cpc = 0.01
                
            actual_cpc = min(actual_cpc, winner['max_bid'])
            
            winner['total_impressions'] += 1
            base_ctr = 0.04
            qs_multiplier = winner['quality_score'] / 10
            simulated_ctr = base_ctr * (1 + qs_multiplier)
            
            click = np.random.random() < simulated_ctr
            conversion = False
            
            if click:
                winner['total_clicks'] += 1
                if winner['remaining_budget'] >= actual_cpc:
                    winner['total_spent'] += actual_cpc
                    winner['remaining_budget'] -= actual_cpc
                    base_cvr = 0.05
                    lp_score = (winner.get('page_speed', 0.5) + winner.get('conversion_forms', 0.5)) / 2
                    simulated_cvr = base_cvr * (1 + lp_score)
                    conversion = np.random.random() < simulated_cvr
                    if conversion:
                        winner['total_conversions'] += 1
            
            auction_result = {
                'search_query': search_query, 'user_location': user_location,
                'user_income': user_income_tier, 'winner': winner['name'],
                'winner_type': winner['type'], 'ad_rank': winner_ad_rank,
                'actual_cpc': actual_cpc, 'click': click, 
                'conversion': conversion, 'timestamp': pd.Timestamp.now()
            }
            
            self.auction_history.append(auction_result)
            return auction_result
        return None

    def run_campaign(self, days=30, searches_per_day=1000):
        print(f"\n🎯 启动 {days}天广告战役模拟")
        print("=" * 50)
        
        locations = ['Center City', 'Main Line', 'Northeast Philly', 'South Philly', 'Jersey Shore']
        income_tiers = ['low', 'medium', 'high']
        search_queries = [
            'used BMW Philadelphia', 'certified pre owned cars Philly',
            'best used car dealer near me', 'luxury SUV Philadelphia'
        ]
        
        for day in range(1, days + 1):
            daily_searches = np.random.poisson(searches_per_day)
            for _ in range(daily_searches):
                query = np.random.choice(search_queries)
                location = np.random.choice(locations)
                income = np.random.choice(income_tiers, p=[0.4, 0.4, 0.2])
                self.simulate_search_auction(query, location, income)
            
            for dealer in self.dealers:
                dealer['remaining_budget'] = dealer['daily_budget']
                
            if day % 10 == 0:
                print(f"📅 第{day}天完成 | 拍卖次数: {len(self.auction_history):,}")
        
        print("✅ 战役模拟完成!")
        self.generate_performance_report()

    def generate_performance_report(self):
        print("\n" + "=" * 80)
        print("🎪 LORD BRIDEGROOM 生态系统分析报告")
        print("=" * 80)
        
        performance_data = []
        for dealer in self.dealers:
            imp = dealer['total_impressions']
            clk = dealer['total_clicks']
            conv = dealer['total_conversions']
            spent = dealer['total_spent']
            
            ctr = (clk / imp * 100) if imp > 0 else 0
            cvr = (conv / clk * 100) if clk > 0 else 0
            cpc = spent / clk if clk > 0 else 0
            cost_per_conv = spent / conv if conv > 0 else 0
            
            estimated_sales = conv * 0.25
            estimated_profit = estimated_sales * 2000
            roi = ((estimated_profit - spent) / spent * 100) if spent > 0 else 0
            
            performance_data.append({
                'Dealer': dealer['name'], 'Type': dealer['type'],
                'Quality_Score': dealer['quality_score'], 'Impressions': imp,
                'Clicks': clk, 'Conversions': conv, 'Total_Spent': spent,
                'CTR (%)': ctr, 'CVR (%)': cvr, 'CPC ($)': cpc,
                'Cost/Conversion ($)': cost_per_conv, 'Estimated_ROI (%)': roi
            })
        
        perf_df = pd.DataFrame(performance_data)
        
        print("\n📈 经销商性能排名:")
        display_cols = ['Dealer', 'Type', 'Quality_Score', 'Clicks', 'Conversions', 'CPC ($)', 'Estimated_ROI (%)']
        ranked_df = perf_df[display_cols].round(2).sort_values('Conversions', ascending=False)
        print(ranked_df.to_string(index=False))
        
        self.create_visualizations(perf_df)
        return perf_df

    def create_visualizations(self, perf_df):
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('LORD BRIDEGROOM 战略分析', fontsize=16, fontweight='bold')
        
        # 质量得分 vs ROI
        axes[0,0].scatter(perf_df['Quality_Score'], perf_df['Estimated_ROI (%)'], 
                         s=perf_df['Conversions']*20, alpha=0.7)
        axes[0,0].set_xlabel('质量得分')
        axes[0,0].set_ylabel('预估ROI (%)')
        axes[0,0].set_title('质量得分投资回报分析')
        
        # 市场份额
        click_share = perf_df.groupby('Type')['Clicks'].sum()
        axes[0,1].pie(click_share.values, labels=click_share.index, autopct='%1.1f%%')
        axes[0,1].set_title('点击量市场份额')
        
        # 效率对比
        types_data = perf_df.groupby('Type').agg({
            'Cost/Conversion ($)': 'mean',
            'CVR (%)': 'mean'
        }).reset_index()
        x = np.arange(len(types_data))
        width = 0.35
        axes[1,0].bar(x - width/2, types_data['Cost/Conversion ($)'], width, label='转化成本($)')
        axes[1,0].bar(x + width/2, types_data['CVR (%)'], width, label='转化率(%)')
        axes[1,0].set_xticks(x)
        axes[1,0].set_xticklabels(types_data['Type'], rotation=45)
        axes[1,0].legend()
        axes[1,0].set_title('各类型效率对比')
        
        # ROI分布
        axes[1,1].barh(perf_df['Dealer'], perf_df['Estimated_ROI (%)'])
        axes[1,1].set_title('各经销商ROI分布')
        axes[1,1].set_xlabel('预估ROI (%)')
        
        plt.tight_layout()
        plt.show()

def main():
    """主执行函数"""
    print("=" * 70)
    print("LORD BRIDEGROOM - 大费城汽车广告生态系统")
    print("三位一体的专家: 商业实战 × 算法创新 × 经济学直觉")
    print("=" * 70)
    
    platform = PhiladelphiaAutoAdPlatform()
    
    # 构建真实生态系统
    dealer_configs = [
        {
            'name': 'Keenan Motors', 'type': 'Large Independent',
            'daily_budget': 80, 'max_bid': 4.5,
            'target_locations': ['Main Line', 'Center City', 'Northeast Philly'],
            'inventory_focus': 'luxury', 'page_speed': 0.8, 'mobile_friendly': 0.9,
            'conversion_forms': 0.7, 'trust_signals': 0.8, 'keyword_match': 0.8,
            'ad_copy_quality': 0.9, 'ad_extensions': 0.8, 'historical_ctr': 0.7,
            'industry_benchmark': 0.8, 'competitor_gap': 0.6
        },
        {
            'name': 'Hertz Car Sales', 'type': 'Large Independent',
            'daily_budget': 70, 'max_bid': 4.0,
            'target_locations': ['Center City', 'Jersey Shore'],
            'inventory_focus': 'diverse', 'page_speed': 0.9, 'mobile_friendly': 0.9,
            'conversion_forms': 0.6, 'trust_signals': 0.9, 'keyword_match': 0.7,
            'ad_copy_quality': 0.8, 'ad_extensions': 0.9, 'historical_ctr': 0.8,
            'industry_benchmark': 0.9, 'competitor_gap': 0.7
        },
        {
            'name': 'CarMax Philadelphia', 'type': 'Large Chain',
            'daily_budget': 120, 'max_bid': 5.0,
            'target_locations': ['Main Line', 'Center City', 'Northeast Philly', 'South Philly', 'Jersey Shore'],
            'inventory_focus': 'diverse', 'quality_score': 7.0
        }
    ]
    
    for config in dealer_configs:
        platform.add_dealer(config)
    
    # 运行模拟
    platform.run_campaign(days=30, searches_per_day=800)
    
    print("\n🎉 模拟完成! LORD BRIDEGROOM的战略洞察已就绪。")

if __name__ == "__main__":
    main()