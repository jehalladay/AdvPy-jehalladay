#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <ctype.h>
#include <vector>
#include <utility>
#include <cstring>
#include <cmath>
#include <iomanip>

using namespace std;

class TestCase {  // This class is an an abstract class
	protected:
	string name;
	public:
	TestCase(string newName) {
		name=newName;
	}
	bool test() {
		cout << "Test " << name << endl;
		bool retval=doTest();
		cout << "End Test " << name;
		if (retval) cout << "->Passed" << endl;
		else cout << "->Failed" << endl;
		return retval;
	}
	virtual bool doTest()=0; // This is a pure virtual function
};

vector<TestCase *> testcases;

enum TokenType{OPEN_PAREN,CLOSE_PAREN,END_OF_TEXT,
			   KEYWORD,IDENTIFIER,LITERAL,COMMA,EQUALS};

string tokenString(TokenType t) {
		switch(t) {
			case KEYWORD: 
				return "KEYWORD";
			case IDENTIFIER: return "IDENTIFIER";
			case LITERAL: return "LITERAL";
			case COMMA: return "COMMA";
			case EQUALS: return "EQUALS";
			case OPEN_PAREN : return "OPEN_PAREN";
			case CLOSE_PAREN : return "CLOSE_PAREN";
			case END_OF_TEXT : return "END_OF_TEXT";
			default: return "UNRECOGNIZED";
		};
}

class Token {
	public:
	TokenType type;
	string value; 
	Token(TokenType newType=UNRECOGNIZED,string newValue="") {
		type=newType;
		value=newValue;
	}
	friend ostream & operator <<(ostream &out,const Token &token) {
		return out <<"Token:" << tokenString(token.type)<<":"<<token.value;
	}
};

const unsigned LEFT=0;
const unsigned RIGHT=1;

class ASTNode {
	Token token;
	vector<ASTNode *> children;
	public:
	ASTNode(Token newToken,ASTNode *left=NULL,ASTNode *right=NULL){
		token=newToken;
		if (left!=NULL) children.push_back(left);
		if (right!=NULL) children.push_back(right);
	}
	void addChild(ASTNode *child){
		children.push_back(child);
	}
	/*vector<ASTNode*> getChildren() {
		return children;
	}*/
	Token getToken() {
		return token;
	}
	ASTNode * childAt(unsigned i) {
		if (i<children.size()) 
		  return children[i];
		else 
		  return NULL;
	}
	unsigned size() {
		return children.size();
	} 
	void print(ostream &out,int depth=0) {
		out << setw(depth) << setfill(' ') << ' ';
		out << token << endl;
		for (auto child:children) child->print(out,depth+1);
	}
};

class Result {
	public:
	bool success;
	ASTNode *subtree;
	Result(bool newSuccess=false,ASTNode *newSubtree=NULL) {
		success=newSuccess;
		subtree=newSubtree;
	}
	void print(ostream &out) {
		out << "Result " << (success?"true":"false")<< endl;
		subtree->print(out);
	}
};

class Tokenizer {
	int linepos,charpos;
	string text;
	unsigned pos;
	public:
	static string filename;
	Result error(string message) {
		cerr << filename<<':'<<linepos<<':' << message << endl;	
		return Result(false);
	}
	Result message(string message,ASTNode *subtree=NULL) {
		cout << filename<<':'<<linepos<<':' << message <<": Next Token "<<peek() << " next text:" <<text.substr(pos,10) <<endl;	
		return Result(true,subtree);
	}
	Tokenizer(){
		text="";
	}
	void readFile(string newFilename) {
		ifstream file(newFilename);
		Tokenizer::filename=newFilename;
		stringstream buffer;
		buffer << file.rdbuf();
		text=buffer.str();
		pos=0;
		linepos=1;
		charpos=1;
	}
	void setText(string newText="") {
		text=newText;
		pos=0;
		linepos=1;
		charpos=1;
	}
	Token next() {
		// Keep track where we are in the text and produce the next token
		Token p=peek();
		pos+=p.value.size();
		return p;
	}
	Token peek() {
		// produce what the next token will be but don't consume
		//cout << "Next character is " << text[pos] << endl;
		while (pos< text.size() && isspace(text[pos])){
		  if (text[pos]=='\n') linepos++;
		  pos++;
	    }
		if (text[pos]=='{') { 
		  while (pos< text.size() && text[pos]!='}') {
		    if (text[pos]=='\n') linepos++;
		    pos++;
		  }
		  pos++;
		}
		char c=text[pos];
		if (pos>=text.size()) return Token(END_OF_TEXT,"");
		if (c=='(')
			return Token(OPEN_PAREN,text.substr(pos,1));
		if (c==')')
			return Token(CLOSE_PAREN,text.substr(pos,1));
		if (c=='=')
			return Token(EQUALS,text.substr(pos,1));
		if (c==',')
			return Token(COMMA,text.substr(pos,1));
		if (isalpha(c)) {
			unsigned newpos=pos;
			while (newpos<text.size() && isalpha(text[newpos]))
			  newpos++;
			string value=text.substr(pos,newpos-pos);
			if (value=="A"||value=="B") return Token(LITERAL,value);
			if (value=="let" || value=="in" || value=="end" || value=="val" || value=="fun" ||
			    value=="turn" || value=="sew") 
			  return Token(KEYWORD,value);
			return Token(IDENTIFIER,value);
		}
		return Token(UNRECOGNIZED,"");
	}
};
string Tokenizer::filename;


class Parser {
	Tokenizer tokens;
	public:
	Token peek() { return tokens.peek(); }
	Tokenizer& getTokenizer() { return tokens; }
	Parser(string newFilename) { 
		tokens=Tokenizer();
		tokens.readFile(newFilename); 
	}
	Result letExpression(Tokenizer &t) {
		Token let=t.next();
		if (let.type==KEYWORD && let.value=="let") {
			Result result=declarations(t);
			if (result.success) {
				Token tok=t.next();
				if (tok.type==KEYWORD && tok.value=="in") {
					Result result2=expression(t);
					if (result2.success) {
						tok=t.next();
						if (tok.type==KEYWORD && tok.value=="END") {
							ASTNode *tree=new ASTNode(let,result.subtree,result2.subtree);
						  return t.message("Success in reading let expression",tree);
					}else 
					  return t.error("Error in expression");
				}
				else 
				  return t.error("Expected in keyword");
			} else 
			  return t.error("Error in declarations in let statement");
		} else 
		  return t.error("Expected let before expression");
	}
	Result declarations(Tokenizer &t) {
		Token tok=t.next();
		if (tok.type==KEYWORD && tok.value=="fun") {
		}
		if (tok.type==KEYWORD && tok.value=="val") {
			Token id=t.next();
			if (id.type==IDENTIFIER) {
				Token tok=t.next();
				if (tok.type==EQUALS) {
					Result result=expression(t);
					if (result.success) {
						return t.message("Success finding val declaration",new ASTNode(id,result.subtree));
					} else 
					return t.error("No expression found in val declaration");
				} else 
				return t.error("No = found in val declaraion");
			} else
			return t.error("No identifier found in val declaration");
		}
		return t.error("Expect fun or val");
	}
	Result expression(Tokenizer &t) {
		// <expression>::=A|B|turn(<expression>)|sew(<expression>,<expression>)
		Token tok=t.next();
		if (tok.type==LITERAL) return t.message("Found Literal",new ASTNode(tok));
		if (tok.type==KEYWORD && tok.value=="turn") {
			Token paren=t.next();
			if (paren.type==OPEN_PAREN) {
				Result result=expression(t);
				if (result.succes) {
					paren=t.next();
					if (paren.type==CLOSE_PAREN) 
					  return t.message("Found turn expression",new ASTNode(tok,result.subtree);
					else
					  return t.error("Missing ) in turn");
				} else
				  return t.error("Expression not found in turn");
			} else 
			  return t.error("Missing ( in turn");
		}
		if (tok.type==KEYWORD && tok.value=="sew") {
			Token paren=t.next();
			if (paren.type==OPEN_PAREN) {
				Result result=expression(t);
				if (result.succes) {
					token comma=t.next();
					if (comma.type==COMMA)
						Result result2,expression(t);
						if (result2.success) {
							paren=t.next();
							if (paren.type==CLOSE_PAREN) {
					          return t.message("Found sew expression",new ASTNode(tok,result.subtree,result2.subtree);
							}else
							return t.error("Missing ) in turn");
						} else 
						  return t.error("Expression not found for second argument of sew");
					  } else 
					    return t.error(", missing in sew expression");
				} else
				  return t.error("Expression not found in sew");
			} else 
			  return t.error("Missing ( in sew");
		}
		return t.error("Expect A, B, sew or turn");
	}
};

class TokenizerTest:public TestCase {  // Tokenizer Test at most 100 tokens
	protected:
		string text;
		bool shouldFail;
	public:
	    TokenizerTest(string newText=".",bool newShouldFail=false) :TestCase("TokenizerTest"){
			text=newText;
			shouldFail=newShouldFail;
		}
	virtual bool doTest() {
		Tokenizer t;
		t.setText(text);
		int count=0;
		int status=0;
		Token token;
		do {
			token=t.next();
			cout << token << endl;
			if (token.type==UNRECOGNIZED) { 
				t.error(" Unrecognized Token ");
				status=1;
			}
			count++;
		} while (token.type!=END_OF_TEXT && count<100);
		return status==0;
    }
};

class TokenizerTestGood:public TokenizerTest {
	public:
		TokenizerTestGood():TokenizerTest("{This is a comment}var * 	2.0E10 /12 \n+ 6"){
			name="TokenizerTestGood "+name;
		}
};

class ParserTest:public TestCase {
	protected:
		Parser *p;
		bool shouldFail;
	public:
	ParserTest(string newFilename,bool newShouldFail=false):TestCase("ParserTest") {
		p=new Parser(newFilename);
		shouldFail=newShouldFail;
	}
	~ParserTest() {
		delete p;
	}
};

class ParserTestScaleFactor:public ParserTest{
	public:
	ParserTestScaleFactor():ParserTest("ScaleFactor.pas") {
		name="ScaleFactor "+name;
	}
	bool doTest() {
		int count=0;
		while (p->peek().type!=END_OF_TEXT) {
			if (p->scaleFactor(p->getTokenizer()).success) {
				count++;
			}
		}
		return count==3;
	}
};

class ParserTestUnsignedReal:public ParserTest{
	public:
	ParserTestUnsignedReal():ParserTest("UnsignedReal.pas") {
		name="UnsignedReal "+name;
	}
	bool doTest() {
		int count=0;
		while (p->peek().type!=END_OF_TEXT) {
			if (p->unsignedReal(p->getTokenizer()).success) {
				count++;
			}
		}
		return count==1;
	}
};

class ParserWholeEnchilada:public ParserTest{
	public:
	ParserWholeEnchilada():ParserTest("WholeEnchilada.pas") {
		name="UnsignedReal "+name;
	}
	bool doTest() {
		int count=0;
		while (p->peek().type!=END_OF_TEXT) {
			cout << "Expression Count is "<< count << endl;
			if (p->expression(p->getTokenizer()).success) {
				count++;
			}
		}
		return count==1;
	}
};

class IntepreterTest:public ParserTest{
	public:
	IntepreterTest():ParserTest("Interpreter.pas") {
		name="Interpreter "+name;
	}
	bool doTest() {
		int count=0;
		while (p->peek().type!=END_OF_TEXT && count<10) {
			cout << "Expression Count is "<< count << endl;
			Result r;
			if ((r=p->expression(p->getTokenizer())).success) {
				r.print(cout);
				return true;
			}
			count++;
		}
		return false;
	}
};

bool runTests() {
//	testcases.push_back(new TokenizerTest());
//	testcases.push_back(new TokenizerTestGood());
//	testcases.push_back(new ParserTestScaleFactor());
//	testcases.push_back(new ParserTestUnsignedReal());
//	testcases.push_back(new ParserWholeEnchilada());
	testcases.push_back(new IntepreterTest());
	bool success=true;
	for (auto test:testcases)
		if (!test->test()) success=false;
	if (success) {
		cout << "All passed" << endl;
		return true;
	}
	cerr << "Failed some test"<<endl; 
	return false;	
}

int main(int argc,char **argv) {
	if (argc<2) {
		cerr<<"Expression <filename>" << endl;
		return -1;
	}
    Parser p(argv[1]);
    int status=0;
    if(!runTests()) status=1;
	return status;
}
