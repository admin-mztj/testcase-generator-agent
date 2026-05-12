class TestCaseAgent:
    def generate(self, content):
        lines = content.split("\n")
        cases = []
        case_id = 1

        for line in lines:
            line = line.strip()
            if not line or len(line) < 5:
                continue

            # 功能测试用例
            cases.append({
                "用例ID": f"TC-{case_id}",
                "模块": "主功能",
                "用例类型": "功能测试",
                "测试点": line[:20],
                "测试步骤": f"1. 进入系统页面\n2. 执行操作：{line[:30]}\n3. 检查结果是否符合预期",
                "预期结果": "功能正常执行，界面无报错，符合需求文档",
                "优先级": "中"
            })
            case_id += 1

            # 边界测试用例
            cases.append({
                "用例ID": f"TC-{case_id}",
                "模块": "边界场景",
                "用例类型": "边界测试",
                "测试点": line[:18] + "边界值",
                "测试步骤": "1. 输入边界数据\n2. 提交/触发功能\n3. 观察系统反应",
                "预期结果": "系统正常处理，无崩溃、无异常",
                "优先级": "高"
            })
            case_id += 1

            # 异常测试用例
            cases.append({
                "用例ID": f"TC-{case_id}",
                "模块": "异常处理",
                "用例类型": "异常测试",
                "测试点": line[:18] + "异常场景",
                "测试步骤": "1. 输入非法/空值/超长数据\n2. 强制中断操作流程\n3. 验证提示",
                "预期结果": "系统给出友好错误提示，不闪退、不卡死",
                "优先级": "中"
            })
            case_id += 1

        return cases