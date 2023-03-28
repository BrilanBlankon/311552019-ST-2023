/*
  Ref:
  * https://llvm.org/doxygen/
  * https://llvm.org/docs/GettingStarted.html
  * https://llvm.org/docs/WritingAnLLVMPass.html
  * https://llvm.org/docs/ProgrammersManual.html
 */
#include "lab-pass.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/Instructions.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/BasicBlock.h"
#include "llvm/IR/IRBuilder.h"
#include "llvm/IR/Constants.h"

#include "llvm/IR/Value.h"
#include "llvm/Support/raw_ostream.h"

#include <sstream>

using namespace llvm;

char LabPass::ID = 0;

static Constant* getI8StrVal(Module &M, char const *str, Twine const &name) {
  LLVMContext &ctx = M.getContext();

  Constant *strConstant = ConstantDataArray::getString(ctx, str);

  GlobalVariable *gvStr = new GlobalVariable(M, strConstant->getType(), true,
    GlobalValue::InternalLinkage, strConstant, name);

  Constant *zero = Constant::getNullValue(IntegerType::getInt32Ty(ctx));
  Constant *indices[] = { zero, zero };
  Constant *strVal = ConstantExpr::getGetElementPtr(Type::getInt8PtrTy(ctx),
    gvStr, indices, true);

  return strVal;
}

static FunctionCallee printfPrototype(Module &M) {
  LLVMContext &ctx = M.getContext();

  FunctionType *printfType = FunctionType::get(
    Type::getInt32Ty(ctx),
    { Type::getInt8PtrTy(ctx) },
    true);

  FunctionCallee printfCallee = M.getOrInsertFunction("printf", printfType);

  return printfCallee;
}

bool LabPass::doInitialization(Module &M) {
  return true;
}

static void dumpIR(Function &F)
{
  for (auto &BB : F) {
    errs() << "BB: " << "\n";
    errs() << BB << "\n";
  }
}

bool LabPass::runOnModule(Module &M) {
  errs() << "runOnModule\n";
  LLVMContext &ctx = M.getContext();
  FunctionCallee printfCallee = printfPrototype(M);
  Type *Int32Ty = Type::getInt32Ty(M.getContext());
  GlobalVariable *depth = new GlobalVariable(M, Int32Ty, false,
    GlobalValue::ExternalLinkage, nullptr, "depth");
  depth->setInitializer(ConstantInt::get(ctx,APInt(32,0)));
  
  for (auto &F : M) {
    if (F.empty()) {
      continue;
    } 
    
    BasicBlock &Bstart = F.front();
    BasicBlock &Bend = F.back();

    Instruction &Istart = Bstart.front();
    IRBuilder<> BuilderStart(&Istart);
    
    std::stringstream ss;
    ss << std::hex << reinterpret_cast<uintptr_t>(&F);
    std::string address_str = ss.str();
    Constant *stackBofMsg = getI8StrVal(M, (F.getName() + ": %p\n").str().c_str(), "testMsg");
    Value *print_format = BuilderStart.CreateGlobalStringPtr("%*c");
    auto *load = BuilderStart.CreateLoad(Type::getInt32Ty(ctx),depth);
    if(F.getName().str() != "main"){
          BuilderStart.CreateCall(printfCallee, { print_format,load,ConstantInt::get(Type::getInt8Ty(ctx), ' ')});
    }
    BuilderStart.CreateCall(printfCallee, { stackBofMsg,&F});

    auto *loadinc = BuilderStart.CreateLoad(Type::getInt32Ty(ctx),depth);
    auto *inc = BuilderStart.CreateAdd(loadinc,ConstantInt::get(ctx, APInt(32, 1)));
    BuilderStart.CreateStore(inc, depth);
    
    Instruction &Isend = Bend.back();
    IRBuilder<> BuilderEnd(&Isend);
    auto *loadsub = BuilderStart.CreateLoad(Type::getInt32Ty(ctx),depth);
    auto *sub = BuilderEnd.CreateSub(loadsub,ConstantInt::get(ctx, APInt(32, 1)));
    BuilderEnd.CreateStore(sub, depth);

    errs() << F.getName() << "\n";
    dumpIR(F);
  }

  return true;
}

static RegisterPass<LabPass> X("labpass", "Lab Pass", false, false);
